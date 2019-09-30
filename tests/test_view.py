import pytest
import json
import config

from app        import create_app
from sqlalchemy import create_engine, text
from .          import data_setup

database = create_engine(config.test_config['DB_URL'], encoding='utf-8', max_overflow = 0)

@pytest.fixture
def api():
    app = create_app(config.test_config)
    app.config['TEST'] = True
    api = app.test_client()

    return api


def setup_function():
    data_setup.setup_test_data(database)

def teardown_function():
    database.execute(text('SET FOREIGN_KEY_CHECKS=0'))
    database.execute(text('TRUNCATE posts'))
    database.execute(text('TRUNCATE reviews'))
    database.execute(text('SET FOREIGN_KEY_CHECKS=1'))
    
def get_test_post(post_id):
    row = database.execute(text('''
        SELECT
            id,
            post_text,
            img,
            total_like,
            author
        FROM posts
        WHERE id = :post_id
        AND is_deleted = 0
    '''), {
        'post_id' : post_id
    }).fetchone()

    return {
        'id': row['id'],
        'author': row['author'],
        'img': row['img'],
        'text': row['post_text'],
        'like': row['total_like']
    } if row else None


def get_test_review(review_id):
    row = database.execute(text('''
        SELECT
            id,
            review_text,
            author,
            post_id
        FROM reviews
        WHERE id = :review_id
        AND is_deleted = 0
    '''), {
        'review_id' : review_id
    }).fetchone()

    return {
        'id': row['id'],
        'author': row['author'],
        'text': row['review_text'],
        'post_id': row['post_id']
    } if row else None


## --------------------------------------

def test_get_timeline(api):
    resp = api.get(
        '/timeline',
        content_type = 'application/json'
    )

    assert resp.json == [{
        'post_id': 3,
        'img': 'url3'
    },{
        'post_id': 2,
        'img': 'url2'
    },{
        'post_id': 1,
        'img': 'url1'
    }]


def test_new_post(api):
    good_data = {
        'img': 'url!',
        'author': 'testman',
        'text': '테스트 입력합니다.'
    } 

    good_resp = api.post(
        '/post',
        data = json.dumps(good_data),
        content_type = 'application/json'
    )

    assert good_resp.status == '200 OK'

    bad_data = {
        'img': 'badbad',
        'author': 'errorman',
        'test': 'error 입력합니다.'
    } 

    bad_resp = api.post(
        '/post',
        data = json.dumps(bad_data),
        content_type = 'application/json'
    )

    assert bad_resp.status == '400 BAD REQUEST'


def test_get_post(api):
    resp = api.get(
        '/post/1',
        content_type = 'application/json'
    )
    
    post = resp.json
    post_test = get_test_post(1)

    assert post['text'] == post_test['text']
    assert post['reviews'][1]['text'] == get_test_review(1)['text']

    bad_resp = api.get(
        '/post/10',
        content_type = 'application/json'
    )

    assert bad_resp.json == None
    assert bad_resp.status == '400 BAD REQUEST'


def test_delete_post(api):
    resp = api.post(
        '/post/delete',
        data = json.dumps({'post_id': 2}),
        content_type = 'application/json'
    )


def test_get_reviews(api):
    resp = api.get(
        '/reviews/1',
        content_type = 'application/json'
    )

    assert len(resp.json) == 2
    assert resp.json[0]['review_id'] == 2


def test_new_review(api):
    new_review = {
        'author': 'testman',
        'text': 'insert review',
        'post_id': 2
    }

    resp = api.post(
        '/reviews',
        data = json.dumps(new_review),
        content_type = 'application/json'
    )
    
    assert resp.json[0]['text'] == new_review['text']
    assert len(resp.json) == 2


def test_delete_review(api):
    resp = api.post(
        '/reviews/delete',
        data = json.dumps({
            'post_id': 2,
            'review_id': 3
        }),
        content_type = 'application/json'
    )

    assert resp.status == '200 OK'
    assert resp.json == []
    
    assert get_test_review(3) == None


def test_add_like(api):
    post_id = 1
    like_before = get_test_post(post_id)['like']
    resp = api.post(
        '/like',
        data = json.dumps({'post_id':post_id}),
        content_type = 'application/json'
    )
    like_after = get_test_post(post_id)['like']

    assert like_before == like_after - 1


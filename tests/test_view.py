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

    assert bad_resp.status != '400 BAD REQUEST'


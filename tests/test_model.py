import pytest
import config

from model      import WestaDao
from sqlalchemy import create_engine, text
from .          import data_setup
from errors     import InvalidRequestError


database = create_engine(config.test_config['DB_URL'], encoding = 'utf-8', max_overflow=0)


@pytest.fixture
def westa_dao():
    return WestaDao(database)


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

def test_insert_post(westa_dao):
    new_post = {
        'img': 'url!',
        'author': 'testman',
        'text': '테스트 입력합니다.'
    }

    post_id = westa_dao.insert_post(new_post)
    post_data = get_test_post(post_id)

    assert post_id == 4
    assert post_data['img'] == new_post['img']
    assert post_data['author'] == new_post['author']
    assert post_data['text'] == new_post['text']

    error_post = { 'img': 'asdfad' }
    new_error = westa_dao.insert_post(error_post)
    assert new_error == None 

    error_post2 = { 'asdf': 123 }
    new_error2 = westa_dao.insert_post(error_post2)
    assert new_error2 == None


def test_get_timeline(westa_dao):
    timeline = westa_dao.get_timeline()

    assert len(timeline) == 3
    assert timeline == [{
        'post_id': 3,
        'img': 'url3'
    },{
        'post_id': 2,
        'img': 'url2'
    },{
        'post_id': 1,
        'img': 'url1'
    }]
    

def test_get_post(westa_dao):
    post = westa_dao.get_post(2)
    post_check = get_test_post(2)

    assert post['author'] == post_check['author']
    assert post['text'] == post_check['text']
    assert post['like'] == post_check['like']


def test_delete_post(westa_dao):
    count = westa_dao.delete_post(2)

    assert count == 2
    assert get_test_post(2) == None
    assert get_test_review(3) == None


def test_get_reviews(westa_dao):
    reviews = westa_dao.get_reviews(1)
    
    assert reviews[0]['review_id'] == 2
    assert reviews[0]['text'] == 'review2'
    assert reviews[1]['author'] == '테스트맨1'


def test_insert_review(westa_dao):
    new_review = {
        'author': 'testman',
        'text': 'insert review',
        'post_id': 2
    }

    review_id = westa_dao.insert_review(new_review)
    review_test = get_test_review(review_id)

    assert review_test['text'] == new_review['text']

    error_data = {
        'author': 'errorman',
        'text': 'error!!!',
        'post_id': 90
    }
    
    error_result = westa_dao.insert_review(error_data)
    assert error_result == None


def test_delete_review(westa_dao):
    post_id = 2
    new_review = {
        'author': 'testman',
        'text': 'insert review',
        'post_id': post_id
    }

    review_id = westa_dao.insert_review(new_review)
    review_test = get_test_review(review_id)
    assert new_review['text'] == review_test['text']

    count1 = westa_dao.delete_review(post_id, review_id)
    assert count1 == 1
    assert get_test_review(review_id) == None

    count2 = westa_dao.delete_review(1, 10)
    assert count2 == 0


def test_add_like(westa_dao):
    like_before = get_test_post(3)['like']
    like_after = westa_dao.add_like(3)['like']

    assert like_after == 4
    assert like_before == like_after - 1

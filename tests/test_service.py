import pytest
import config

from model      import WestaDao
from service    import WestaService
from sqlalchemy import create_engine, text
from .          import data_setup

database = create_engine(config.test_config['DB_URL'], encoding='utf-8', max_overflow = 0)

@pytest.fixture
def westa_service():
    return WestaService(WestaDao(database), config.test_config)

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


def test_new_post(westa_service):
    new_post = {
        'img': 'url!',
        'author': 'testman',
        'text': '테스트 입력합니다.'
    }

    bad_data = {
        'img': 'badbad',
        'author': 'errorman',
        'test': 'error 입력합니다.'
    }

    new_post_list = westa_service.new_post(new_post)
    assert new_post_list[0]['img'] == new_post['img']

    errrr = westa_service.new_post(bad_data)
    assert errrr == None 


def test_get_post(westa_service):
    post = westa_service.get_post(1)
    post_test = get_test_post(1)

    assert post['text'] == post_test['text']
    assert post['reviews'][1]['text'] == get_test_review(1)['text']

    post_none = westa_service.get_post(10)

    assert post_none == None
    

def test_new_review(westa_service):
    new_review = {
        'author': 'testman',
        'text': 'insert review',
        'post_id': 2
    }

    new_review_list = westa_service.new_review(new_review)
    assert new_review_list[0]['text'] == new_review['text'] 

    error_data = {
        'author': 'errorman',
        'text': 'error!!!',
        'post_id': 90
    }

    errors = westa_service.new_review(error_data)
    assert errors == None


def test_delete_review(westa_service):
    post_id = 2
    new_review = {
        'author': 'testman',
        'text': 'insert review',
        'post_id': post_id
    }

    review_id = westa_service.westa_dao.insert_review(new_review)
    review_test = get_test_review(review_id)
    assert new_review['text'] == review_test['text']

    reviews = westa_service.delete_review( post_id, review_id)
    assert len(reviews) == 1
    assert reviews[0]['review_id'] == 3
    

    

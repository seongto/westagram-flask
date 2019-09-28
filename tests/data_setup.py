
from model      import WestaDao
from sqlalchemy import text


def setup_test_data(database):
    new_posts = [{
        'id': 1,
        'img': 'url1',
        'post_text': 'post1',
        'total_like': 1,
        'author': '테스트맨1'
    },{
        'id': 2,
        'img': 'url2',
        'post_text': 'post2',
        'total_like': 2,
        'author': '테스트맨2'
    },{
        'id': 3,
        'img': 'url3',
        'post_text': 'post3',
        'total_like': 3,
        'author': '테스트맨3'
    }]


    new_reviews = [{
        'id': 1,
        'review_text': 'review1',
        'post_id': 1,
        'author': '테스트맨1'
    },{
        'id': 2,
        'review_text': 'review2',
        'post_id': 1,
        'author': '테스트맨2'
    },{
        'id': 3,
        'review_text': 'review3',
        'post_id': 2,
        'author': '테스트맨3'
    },{
        'id': 4,
        'review_text': 'review4',
        'post_id': 3,
        'author': '테스트맨4'
    },{
        'id': 5,
        'review_text': 'review5',
        'post_id': 3,
        'author': '테스트맨5'
    }]


    database.execute(text('''
        INSERT INTO posts (
            id,
            img,
            post_text,
            total_like,
            author
        ) VALUES (
            :id,
            :img,
            :post_text,
            :total_like,
            :author
        )
    '''), new_posts)

    database.execute(text('''
        INSERT INTO reviews (
            id,
            review_text,
            post_id,
            author
        ) VALUES (
            :id,
            :review_text,
            :post_id,
            :author
        )
    '''), new_reviews)
    

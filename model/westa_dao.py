from sqlalchemy     import text, exc
from errors         import InvalidRequestError

class WestaDao :
    def __init__(self, database):
        self.db = database

    def insert_post(self, new_post):
        try:
            return self.db.execute(text('''
                INSERT INTO posts (
                    author,
                    post_text,
                    img
                ) VALUES (
                    :author,
                    :text,
                    :img
                )
            '''), new_post).lastrowid

        except(exc.StatementError):
            return None

    def get_timeline(self):
        rows = self.db.execute(text('''
            SELECT
                id,
                img,
                created_at
            FROM posts
            WHERE is_deleted = 0
            ORDER BY id DESC
        ''')).fetchall()

        return [{
            'post_id': row['id'],
            'img': row['img']
        } for row in rows ] if rows else None


    def get_post(self, post_id):
        row = self.db.execute(text('''
            SELECT
                author,
                img,
                post_text,
                total_like,
                created_at
            FROM posts
            WHERE is_deleted = 0
            AND id = :post_id
        '''), {'post_id': post_id}).fetchone()

        return {
            'author': row['author'],
            'img': row['img'],
            'text': row['post_text'],
            'like': row['total_like'],
            'created_at': row['created_at']
        } if row else None

    def delete_post(self, post_id):
        count = self.db.execute(text('''
            UPDATE posts
            SET is_deleted = 1
            WHERE id = :post_id
        '''), {'post_id': post_id}).rowcount

        return count

    
    def get_reviews(self, post_id):
        rows = self.db.execute(text('''
            SELECT 
                id,
                author,
                review_text,
                created_at
            FROM reviews
            WHERE post_id = :post_id
            AND is_deleted = 0
            ORDER BY id DESC
        '''), { 'post_id': post_id }).fetchall()

        return[{
            'review_id': row['id'],
            'author': row['author'],
            'text': row['review_text'],
            'created_at': row['created_at']
        } for row in rows ] if rows else None


    def insert_review(self, new_review):
        try:
            return self.db.execute(text('''
                INSERT INTO reviews (
                    author,
                    review_text,
                    post_id
                ) VALUES (
                    :author,
                    :text,
                    :post_id
                )
            '''), new_review).lastrowid

        except(exc.StatementError):
            return None


    def delete_review(self, review_id):
        count = self.db.execute(text('''
            UPDATE reviews
            SET is_deleted = 1
            WHERE id = :review_id
        '''), {'review_id': review_id}).rowcount

        return count


    def add_like(self, post_id):
        self.db.execute(text('''
            UPDATE posts
            SET total_like = total_like + 1
            WHERE id = :post_id
        '''), {'post_id': post_id })

        row = self.db.execute(text('''
            SELECT total_like
            FROM posts
            WHERE id = :post_id
        '''), {'post_id': post_id }).fetchone()

        return { 
            'like': row['total_like']
        } if row else None


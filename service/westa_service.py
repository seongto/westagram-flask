import re


class WestaService:
    def __init__(self, westa_dao):
        self.westa_dao = westa_dao

    def new_post(self, new_post):
        result = self.westa_dao.insert_post(new_post)
        if result != None:
            post_list = self.westa_dao.get_timeline()
            return post_list  
        else:
            return None

    def get_post(self, post_id):
        try:
            post_data = self.westa_dao.get_post(post_id)
            post_data['reviews'] = self.westa_dao.get_reviews(post_id)
            return post_data
        except(TypeError):
            return None
        
    def new_review(self, new_review):
        result = self.westa_dao.insert_review(new_review)

        if result != None:
            reviews = self.westa_dao.get_reviews(new_review['post_id'])
            return reviews
        else:
            return None

    def delete_review(self, post_id, review_id):
        result = self.westa_dao.delete_review(post_id, review_id)
        if result == 1:
            reviews = self.westa_dao.get_reviews(post_id)
            return reviews
        else :
            return None



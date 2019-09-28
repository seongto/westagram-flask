import re


class WestaService:
    def __init__(self, westa_dao, config):
        self.westa_dao = westa_dao
        self.config = config
        

    def new_post(self, new_post):
        self.westa_dao.insert_post(new_post)
        post_list = self.westa_dao.get_timeline()
        return post_list


    def get_post(self, post_id):
        try:
            post_data = self.westa_dao.get_post(post_id)
            post_data['reviews'] = self.westa_dao.get_reviews(post_id)
            return post_data
        except(TypeError):
            return None

        
    def new_review(self, new_review):
        self.westa_dao.insert_review(new_review)
        reviews = self.westa_dao.get_reviews(new_review['post_id'])
        return reviews


    def delete_review(self, credential):
        self.westa_dao.delete_review(credential['review_id'])
        reviews = self.westa_dao.get_reviews(credential['post_id'])
        return reviews



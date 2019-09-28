import re

from flask      import request, jsonify, current_app, Response, g
from flask.json import JSONEncoder
from errors     import InvalidRequestError


## set를 list로 변환하여 JSON으로 변환 가능하게 해주는 커스텀 encoder
class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)

        return JSONEncoder.default(self, obj)


def create_endpoints(app, services):
    westa_service = services.westa_service


    @app.route('/timeline', methods=['GET'])
    def user_registration():
        try:
            timeline = westa_servcie.westa_dao.get_timeline()
            return jsonify(timeline), 200
        except:
            return '', 400

    @app.route('/post', methods=['POST'])
    def new_post():
        try:
            credential = request.json
            post_list = westa_service.new_post(credential)
            if post_list == None:
                raise InvalidRequestError
            return jsonify(post_list), 200

        except(InvalidRequestError):
            return '', 400
            print('what the fuck')
       

    @app.route('/post/<int:post_id>', methods=['GET'])
    def get_post(post_id):
        try:
            post_data = westa_service.get_post(post_id)
            return jsonify(post_data), 200
        except:
            return '', 400

    @app.route('/post/delete', methods=['POST'])
    def delete_post():  
        try:
            credential = request.json()
            result = westa_service.westa_dao.delete_post(credential['post_id'])
            if result != 1:
                raise InvalidRequestError
            return '', 200
        except:
            return '', 400

    @app.route('/reviews/<int:post_id>', methods=['GET'])
    def get_reviews(post_id):
        try:
            review_list = westa_service.westa_dao.get_reviews(post_id)
            return jsonify(review_list), 200
        except:
            return '', 400

    @app.route('/reviews', methods=['POST'])
    def new_review():
        credential = request.json()
        try:
            review_list = westa_service.westa_dao.new_review(credential)
            return jsonify(review_list), 200
        except:
            return '', 400

    @app.route('/review/delete', methods=['POST'])
    def delete_review():
        credential = request.json()
        try:
            review_list = westa_service.delete_review(credential['post_id'], credential['review_id'])
            if review_list == None:
                raise InvalidRequestError
            return jsonify(review_list), 200
        except:
            return '', 400


    @app.route('/like', methods=['POST'])
    def add_like():
        credential = request.json()
        try:
            total_like = westa_service.westa_dao.add_like(credential['post_id'])
            return jsonify(total_like), 200
        except:
            return '', 400




            

       

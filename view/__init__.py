import re

from flask      import request, jsonify, current_app, Response, g
from flask.json import JSONEncoder


## set를 list로 변환하여 JSON으로 변환 가능하게 해주는 커스텀 encoder
class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)

        return JSONEncoder.default(self, obj)




from flask import (
  Blueprint,
  request,
  make_response,
  jsonify
)
from flask.views import MethodView


user_blueprint = Blueprint('users', __name__)

class LoginAPI(MethodView):
  def post(self):
    post_data = request.get_json()










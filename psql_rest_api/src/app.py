from flask import Blueprint
from flask_restful import Api
from src.views.Hello import Hello
from src.views.Category import CategoryResource
from src.views.Comment import CommentResource


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(Hello, '/hello')
api.add_resource(CategoryResource, '/category')
api.add_resource(CommentResource, '/comment')

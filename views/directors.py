from flask import request
from flask_restx import Resource, Namespace
from implemented import director_schema, directors_schema, director_service
from helpers.decorators import auth_required
from parsers import page_parser

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        filters = page_parser.parse_args()
        directors = director_service.get_all(filters)
        return directors_schema.dump(directors), 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    @auth_required
    def get(self, did):
        director = director_service.get_one_by_id(did)
        if director is None:
            return 'Director not found', 404
        return director_schema.dump(director), 200

from flask_restx import Resource, Namespace
from implemented import genre_schema, genres_schema, genre_service
from helpers.decorators import auth_required
from parsers import page_parser

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        filters = page_parser.parse_args()
        genres = genre_service.get_all(filters)
        return genres_schema.dump(genres), 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    @auth_required
    def get(self, gid):
        genre = genre_service.get_one_by_id(gid)
        if genre is None:
            return 'Genre not found', 404
        return genre_schema.dump(genre), 200

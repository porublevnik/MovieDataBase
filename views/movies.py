from flask_restx import Resource, Namespace
from implemented import movie_schema, movies_schema, movie_service
from helpers.decorators import auth_required
from parsers import page_parser
movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    @auth_required
    def get(self):
        filters = page_parser.parse_args()
        movies = movie_service.get_all(filters)
        return movies_schema.dump(movies), 200


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    @auth_required
    def get(self, mid):
        movie = movie_service.get_one_by_id(mid)
        if movie is None:
            return 'Movie not found', 404
        return movie_schema.dump(movie), 200

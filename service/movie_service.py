from dao.movie_dao import MovieDAO

class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self, filters):
        return self.dao.get_all(filters)

    def get_one_by_id(self, mid: int):
        return self.dao.get_one_by_id(mid)

from .model.movie import Movie

class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self, filters):
        page = filters.get('page')
        status = filters.get('status')
        stmt = self.session.query(Movie)
        if status == 'new':
            stmt = stmt.order_by(Movie.year.desc())
        if page is not None:
            stmt = stmt.paginate(page=page, per_page=12).items
        return stmt

    def get_one_by_id(self, mid: int):
        return self.session.query(Movie).get(mid)

    # def get_all_by_director(self, did: int):
    #     return self.session.query(Movie).filter(Movie.director_id == did).all()
    #
    # def get_all_by_genre(self, gid: int):
    #     return self.session.query(Movie).filter(Movie.genre_id == gid).all()
    #
    # def get_all_by_year(self, year: int):
    #     return self.session.query(Movie).filter(Movie.year == year).all()

    def create(self, data):
        movie = Movie(**data)

        self.session.add(movie)
        self.session.commit()

        return movie

    def update(self, movie):

        self.session.add(movie)
        self.session.commit()

        return movie

    def delete(self, movie):

        self.session.delete(movie)
        self.session.commit()

    
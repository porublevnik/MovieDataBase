from .model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self, filters):
        page = filters.get('page')
        stmt = self.session.query(Genre)
        if page is not None:
            stmt = stmt.paginate(page=page, per_page=12).items
        return stmt

    def get_one_by_id(self, gid: int):
        return self.session.query(Genre).get(gid)

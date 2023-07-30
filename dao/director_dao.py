from .model.director import Director

class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self, filters):
        page = filters.get('page')
        stmt = self.session.query(Director)
        if page is not None:
            stmt = stmt.paginate(page=page, per_page=12).items
        return stmt

    def get_one_by_id(self, did: int):
        return self.session.query(Director).get(did)

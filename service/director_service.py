from dao.director_dao import DirectorDAO

class DirectorService:

    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_all(self, filters):
        return self.dao.get_all(filters)

    def get_one_by_id(self, did: int):
        return self.dao.get_one_by_id(did)

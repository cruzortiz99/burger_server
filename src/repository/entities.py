class Entity():
    def save(self):
        raise Exception("debe implementar este elemento")

    def get_all(self):
        raise Exception("debe implementar este elemento")

    def get_by_id(self, id):
        raise Exception("debe implementar este elemento")

    def delete(self, id):
        raise Exception("debe implementar este elemento")

    def update(self, id, entity):
        raise Exception("debe implementar este elemento")

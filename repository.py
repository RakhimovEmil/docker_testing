class Rediska:
    def __init__(self, redis_client):
        self.redis_client = redis_client

    def get(self, key):
        return self.redis_client.get(key)

    def put(self, key, value):
        return self.redis_client.set(key, value)

    def delete(self, key):
        return self.redis_client.delete(key)

    def exists(self, key):
        return self.redis_client.exists(key)


class Mango:
    def __init__(self, db):
        self.mongo_table = db

    def get(self, key):
        return self.mongo_table.find_one({'key': key})['value']

    def put(self, key, value):
        self.mongo_table.insert_one({'key': key, 'value': value})

    def delete(self, key):
        self.mongo_table.delete_one({'key': key})

    def exists(self, key):
        return self.mongo_table.find_one({'key': key})
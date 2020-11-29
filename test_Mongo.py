import unittest
import pymongo
import os
from repository import Mango


class MyTestCase(unittest.TestCase):

    def setUp(self):
        mongo_client = pymongo.MongoClient(host='0.0.0.0', port=27017)
        mongo_table = mongo_client.client['hw9']['cache']
        self.table = Mango(mongo_table)
        os.system('docker run --rm --detach --name emils-mongo-test --publish 27017:27017 mongo')

    def tearDown(self):
        os.system('docker stop emils-mongo-test')

    def test_get_returns_value_from_cache(self):
        self.table.put("key", "value")
        value = self.table.get("key")
        self.assertEqual(value, "value")


if __name__ == '__main__':
    unittest.main()

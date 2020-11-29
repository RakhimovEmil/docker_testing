import json
import pymongo
import redis

from flask import Flask, request, json

from repository import Rediska, Mango
from service import Service

app = Flask(__name__)


@app.route("/storage/<filename>", methods=['GET'])
def get_collection(filename):
    if my_service.get(filename):
        return my_service.get(filename), 200
    return "", 404


@app.route("/storage/<filename>", methods=["PUT"])
def put_collection(filename):
    req = json.dumps(request.get_json())
    if request.is_json:
        my_service.put(filename, req)
        return "", 201
    return "", 400


@app.route("/storage/<filename>", methods=["DELETE"])
def delete_collection(filename):
    my_service.delete(filename)
    return "", 204


if __name__ == '__main__':
    redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)
    cache = Rediska(redis_client)

    mongo_client = pymongo.MongoClient(host='0.0.0.0', port=27017)
    mongo_table = mongo_client['hw9']['storage']
    database = Mango(mongo_table)

    my_service = Service(cache, database)
    app.run(host='0.0.0.0', port=8080)

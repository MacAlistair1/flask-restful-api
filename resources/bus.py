from flask import Response, request
from database.models import Bus
from flask_restful import Resource
import random
import string


class BusesApi(Resource):
    def get(self):
        buses = Bus.objects().to_json()
        return Response(buses, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        body['number_plate'] = "123456"
        bus = Bus(**body).save()
        bus = Bus.objects.get(id=bus.id).to_json()
        return Response(bus, mimetype="application/json", status=200)


class BusApi(Resource):
    def get(self, id):
        bus = Bus.objects.get(id=id).to_json()
        return Response(bus, mimetype="application/json", status=200)

    def put(self, id):
        body = request.get_json()
        Bus.objects.get(id=id).update(**body)
        return '', 200

    def delete(self, id):
        Bus.objects.get(id=id).delete()
        return '', 200

from flask import Blueprint, request
from flask_restful import Api, Resource
from datetime import datetime
from .schemas import TXStatusSchema
from ..models import TXStatus

tx_status_bp = Blueprint('tx_status_bp', __name__)

txStatusSchema = TXStatusSchema()

api = Api(tx_status_bp)

class TXStatusListResource(Resource):
	def get(self):
		spazioStatus = TXStatus.get_all()
		result = txStatusSchema.dump(spazioStatus, many=True)
		return result

class TXStatusRemoveResource(Resource):
	def delete(self, machine):
		toDelete = TXStatus.filter_by_machine(machine)
		for i in toDelete:
			i.delete()
		return 204

	def post(self, machine):
		data = request.get_json()
		now = datetime.now()
		date = now.strftime("%d/%b/%Y %H:%M")
		for check in data['checks']:
			txstatus = TXStatus(machine = machine,
									resource = check['resource'],
									status = check['status'],
									dangerLevel = check['dangerLevel'],
									problemGroup = check['problemGroup'],
									date = date)
			txstatus.save()
		return 201

api.add_resource(TXStatusListResource, '/api/v1.0/txStatus/', endpoint='tx_status_list_resource')
api.add_resource(TXStatusRemoveResource, '/api/v1.0/txStatus/machine/<machine>', endpoint='tx_status_remove_resource')
from flask import Blueprint, request
from flask_restful import Api, Resource
from datetime import datetime
from .schemas import MQStatusSchema
from ..models import MQStatus

mq_status_bp = Blueprint('mq_status_bp', __name__)

mqStatusSchema = MQStatusSchema()

api = Api(mq_status_bp)

class MQStatusListResource(Resource):
	def get(self):
		spazioStatus = MQStatus.get_all()
		result = mqStatusSchema.dump(spazioStatus, many=True)
		return result

class MQStatusRemoveResource(Resource):
	def delete(self, machine):
		toDelete = MQStatus.filter_by_machine(machine)
		for i in toDelete:
			i.delete()
		return 204

	def post(self, machine):
		data = request.get_json()
		now = datetime.now()
		date = now.strftime("%d/%b/%Y %H:%M")
		for check in data['checks']:
			mqstatus = MQStatus(machine = machine,
									resource = check['resource'],
									status = check['status'],
									dangerLevel = check['dangerLevel'],
									problemGroup = check['problemGroup'],
									date = date)
			mqstatus.save()
		return 201

api.add_resource(MQStatusListResource, '/api/v1.0/mqStatus/', endpoint='mq_status_list_resource')
api.add_resource(MQStatusRemoveResource, '/api/v1.0/mqStatus/machine/<machine>', endpoint='mq_status_remove_resource')

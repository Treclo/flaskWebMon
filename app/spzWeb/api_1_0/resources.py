from flask import Blueprint
from flask_restful import Api, Resource
from .schemas import SpzWebSchema
from ..models import SpzWeb

spzweb_bp = Blueprint('spzweb_bp', __name__)

spzWebSchema = SpzWebSchema()

api = Api(spzweb_bp)

class SpzWebListResource(Resource):
	def get(self):
		list = SpzWeb.get_all()
		result = spzWebSchema.dump(list, many=True)
		return result

class SpzWebListResourceById(Resource):
	def put(self, id):
		user = SpzWeb.get_by_id(id)
		user.updateDate()
		return 200

class SpzWebListResourceByT(Resource):
	def put(self, matricula):
		user = SpzWeb.filter_by_t(matricula)
		if user is not None:
			user.updateDate()
		return 200

	def delete(self, matricula):
		user = SpzWeb.filter_by_t(matricula)
		if user is not None:
			user.delete()
		return 204

class SpzWebAddUser(Resource):
	def post(self, matricula, email):
		user = SpzWeb.filter_by_t(matricula)
		if user is None:
			new_user = SpzWeb(matricula = matricula,
								email = email,
								ultimoAcceso = "")
			new_user.updateDate()
		return 201


api.add_resource(SpzWebListResource, '/api/v1.0/spz_web/', endpoint='spz_web_list_resource')
api.add_resource(SpzWebListResourceById, '/api/v1.0/spz_web/<id>', endpoint='spz_web_list_resource_by_id')
api.add_resource(SpzWebListResourceByT, '/api/v1.0/spz_web/matricula/<matricula>', endpoint='spz_web_list_resource_by_t')
api.add_resource(SpzWebAddUser, '/api/v1.0/spz_web/add/<matricula>/<email>', endpoint='spz_web_add')
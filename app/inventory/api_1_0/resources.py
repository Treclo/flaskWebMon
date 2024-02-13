from flask import Blueprint, request
from flask_restful import Api, Resource
from .schemas import InventorySchema
from ..models import Inventory

inventory_bp = Blueprint('inventory_bp', __name__)

inventorySchema = InventorySchema()

api = Api(inventory_bp)

class InventoryListResource(Resource):
	def get(self):
		inventory = Inventory.get_all()
		result = inventorySchema.dump(inventory, many=True)
		return result
	
	def post(self):
		data = request.get_json()
		inventory_dict = inventorySchema.load(data)
		inventoryItem = Inventory(machine = inventory_dict['machine'],
									technology = inventory_dict['technology'],
									version = inventory_dict['version'],
									environment = inventory_dict['environment'],
									scope = inventory_dict['scope'],
									system = inventory_dict['system'],
									architecture = inventory_dict['architecture'],
									resources = inventory_dict['resources'],
									app = inventory_dict['app'],
									ports = inventory_dict['ports'],
									user = inventory_dict['user'],
									password = inventory_dict['password'],
									notes = inventory_dict['notes']
		)
		inventoryItem.save()
		resp = inventorySchema.dump(inventoryItem)
		return resp, 201


class InventoryListResourceById(Resource):
	def get(self, id):
		item = Inventory.get_by_id(id)
		resp = inventorySchema.dump(item)
		return resp

	def delete(self, id):
		item = Inventory.get_by_id(id)
		if item is None:
			return 404
		item.delete()
		return 204

	def put(self, id):
		item = Inventory.get_by_id(id)
		if item is None:
			return 404
		data = request.json
		item.setData(data["mod"], data["data"])

api.add_resource(InventoryListResource, '/api/v1.0/inventory/', endpoint='inventory_list_resource')
api.add_resource(InventoryListResourceById, '/api/v1.0/inventory/<id>', endpoint='inventory_list_resource_by_id')
from marshmallow import fields
from app.ma import ma

class InventorySchema(ma.Schema):
	id = fields.Integer(dump_only=True)
	machine = fields.String()
	technology = fields.String()
	version = fields.String()
	environment = fields.String()
	scope = fields.String()
	system = fields.String()
	architecture = fields.String()
	resources = fields.String()
	app = fields.String()
	ports = fields.String()
	user = fields.String()
	password = fields.String()
	notes = fields.String()
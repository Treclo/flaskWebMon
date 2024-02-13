from marshmallow import fields
from app.ma import ma

class MQStatusSchema(ma.Schema):
	id = fields.Integer(dump_only=True)
	machine = fields.String()
	resource = fields.String()
	status = fields.String()
	dangerLevel = fields.String()
	problemGroup = fields.String()
	date = fields.String()
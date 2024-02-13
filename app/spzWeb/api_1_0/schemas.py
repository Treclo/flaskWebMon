from marshmallow import fields
from app.ma import ma

class SpzWebSchema(ma.Schema):
	id = fields.Integer(dump_only=True)
	matricula = fields.String()
	email = fields.String()
	ultimoAcceso = fields.String()
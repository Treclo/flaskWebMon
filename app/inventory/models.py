from sqlalchemy import UniqueConstraint
from app.db import db, BaseModelMixin

class Inventory(db.Model, BaseModelMixin):
	__tablename__ = 'Inventory'

	id = db.Column(db.Integer, primary_key=True)
	machine = db.Column(db.String, nullable=False)
	technology = db.Column(db.String, nullable=False)
	version = db.Column(db.String)
	environment = db.Column(db.String, nullable=False)
	scope = db.Column(db.String, nullable=False)
	system = db.Column(db.String, nullable=False)
	architecture = db.Column(db.String, nullable=False)
	resources = db.Column(db.String, nullable=False)
	app = db.Column(db.String)
	ports = db.Column(db.String)
	user = db.Column(db.String)
	password = db.Column(db.String)
	notes = db.Column(db.String)
	UniqueConstraint("machine", "technology")

	def __init__(self, machine, technology, version, environment, scope, system, architecture, resources, app, ports, user, password, notes):
		self.machine = machine
		self.technology = technology
		self.version = version
		self.environment = environment
		self.scope = scope
		self.system = system
		self.architecture = architecture
		self.resources = resources
		self.app = app
		self.ports = ports
		self.user = user
		self.password = password
		self.notes = notes

	def setData(self, value, data):
		if (value == "version"):
			self.version = data
			db.session.commit()
		elif (value == "system"):
			self.system = data
			db.session.commit()
		elif (value == "architecture"):
			self.architecture = data
			db.session.commit()
		elif (value == "resources"):
			self.resources = data
			db.session.commit()
		elif (value == "app"):
			self.app = data
			db.session.commit()
		elif (value == "ports"):
			self.ports = data
			db.session.commit()
		elif (value == "user"):
			self.user = data
			db.session.commit()
		elif (value == "password"):
			self.password = data
			db.session.commit()
		elif (value == "notes"):
			self.notes = data
			db.session.commit()

	def __repr__(self):
		return 'Pair({self.machine}, {self.technology})'

	def __str__(self):
		return '{self.machine}, {self.technology}'
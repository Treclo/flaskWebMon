from app.db import db, BaseModelMixin

class SpazioStatus(db.Model, BaseModelMixin):
	__tablename__ = 'SpazioStatus'
	__bind_key__ = 'SpazioStatus'

	id = db.Column(db.Integer, primary_key=True)
	machine = db.Column(db.String, nullable=False)
	status = db.Column(db.String, nullable=False)
	dangerLevel = db.Column(db.String, nullable=False)
	problemGroup = db.Column(db.String, nullable=False)
	date = db.Column(db.String, nullable=False)

	def __init__(self, machine, status, dangerLevel, problemGroup, date):
		self.machine = machine
		self.status = status
		self.dangerLevel = dangerLevel
		self.problemGroup = problemGroup
		self.date = date

	def __repr__(self):
		return 'Pair({self.machine}, {self.status})'

	def __str__(self):
		return '{self.status}'
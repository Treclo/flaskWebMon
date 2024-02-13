from sqlalchemy import UniqueConstraint
from app.db import db, BaseModelMixin
from datetime import datetime

class SpzWeb(db.Model, BaseModelMixin):
	__tablename__ = 'UsersSpzIntranet'

	id = db.Column(db.Integer, primary_key=True)
	matricula = db.Column(db.String, nullable=False)
	email = db.Column(db.String)
	ultimoAcceso = db.Column(db.String)
	UniqueConstraint("matricula")

	def __init__(self, matricula, email, ultimoAcceso):
		self.matricula = matricula
		self.email = email
		self.ultimoAcceso = ultimoAcceso

	def __repr__(self):
		return 'User({self.matricula})'

	def __str__(self):
		return '{self.matricula}'

	def updateDate(self):
		now = datetime.now()
		date = now.strftime("%d/%b/%Y")
		self.ultimoAcceso = date
		self.save()

	@classmethod
	def filter_by_t(self, t):
		return SpzWeb.query.filter_by(matricula=t).first()
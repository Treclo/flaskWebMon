from app.db import db, BaseModelMixin

class TXStatus(db.Model, BaseModelMixin):
	__tablename__ = 'TXStatus'
	__bind_key__ = 'TXSeriesStatus'

	id = db.Column(db.Integer, primary_key=True)
	machine = db.Column(db.String, nullable=False)
	resource = db.Column(db.String, nullable=False)
	status = db.Column(db.String, nullable=False)
	dangerLevel = db.Column(db.String, nullable=False)
	problemGroup = db.Column(db.String, nullable=False)
	date = db.Column(db.String, nullable=False)
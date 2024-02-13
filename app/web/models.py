from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
	__tablename__ = 'Users'

	id = db.Column(db.Integer, primary_key=True)
	user = db.Column(db.String, nullable=False)
	password = db.Column(db.String, nullable=False)
	isAdmin = db.Column(db.Boolean, default=False)

	def __repr__(self):
		return self.user

	def save(self):
		if not self.id:
			db.session.add(self)
		db.session.commit()

	def delete(self):
		db.session.delete(self)
		db.session.commit()

	def set_password(self, password):
		self.password = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password, password)

	@staticmethod
	def get_by_id(id):
		return User.query.get(id)

	@staticmethod
	def get_by_user(user):
		return User.query.filter_by(user=user).first()
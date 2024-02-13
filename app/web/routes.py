from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, logout_user, current_user, login_user
from .models import User

web_bp = Blueprint('web_bp', __name__)

@web_bp.route('/')
@web_bp.route('/login', methods=["GET", "POST"])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('web_bp.inventario'))
	if request.method == "GET":
		return render_template('login.html')
	user = User.get_by_user(request.form.get('user'))
	if user is not None and user.check_password(request.form.get('password')):
		login_user(user, remember=request.form.get('rememberMe'))
		return redirect(url_for('web_bp.inventario'))
	else:
		return redirect(url_for('web_bp.login'))

@web_bp.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('web_bp.login'))

@web_bp.route('/inventario')
@login_required
def inventario():
	return render_template('inventory.html')

@web_bp.route('/spzWeb')
@login_required
def spzWeb():
	return render_template('spazio-web.html')

@web_bp.route('/editItem')
@login_required
def editItem():
	id = request.args.get('id')
	if id is not None:
		return render_template('editItem.html')
	else:
		return redirect(url_for('web_bp.inventario'))

@web_bp.route('/monSpazio')
def monSpazio():
	return render_template('monSpazio.html')

@web_bp.route('/monMQ')
def monMQ():
	return render_template('monMQ.html')

@web_bp.route('/monTX')
def monTX():
	return render_template('monTX.html')

@web_bp.route('/register_user', methods=["GET", "POST"])
@login_required
def register_user():
	if request.method == "GET":
		return render_template('registerUser.html')
	user_name = request.form.get('user')
	password = request.form.get('password')
	isAdmin = request.form.get('isAdmin')
	if (isAdmin == '0'):
		isAdmin = False
	else:
		isAdmin = True
	if (User.get_by_user(user_name) is None):
		user = User(user=user_name, isAdmin=isAdmin)
		user.set_password(password)
		user.save()
	return redirect(url_for('web_bp.inventario'))

@web_bp.route('/change_password', methods=["GET", "POST"])
@login_required
def change_password():
	if request.method == "GET":
		return render_template('changePassword.html')
	#password = request.form.get('password')
	#user = User.get_by_user(current_user)
	#user.set_password(password)
	#user.save()
	return redirect(url_for('web_bp.inventario'))
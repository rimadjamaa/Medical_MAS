from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user
from models.UserModel import User


login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login_rout():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('admin_dashboard'))

        flash('Invalid credentials', 'danger')
        return redirect(url_for('login.login_rout'))

    return render_template("login.html")
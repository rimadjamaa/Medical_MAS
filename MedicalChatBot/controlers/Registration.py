from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_bcrypt import Bcrypt
from extentions import db
from models.UserModel import User

register = Blueprint('register', __name__)
bcrypt = Bcrypt()

@register.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')


        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already registered!', 'danger')
            return redirect(url_for('register.register_user'))

        new_user = User(username=username, email=email, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login.login_rout'))

    return render_template('register.html')

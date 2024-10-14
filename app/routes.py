from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from app import db, bcrypt

routes = Blueprint('routes', __name__)


@routes.route('/')
def index():
    return render_template('index.html')


@routes.route('/register', methods=['GET', 'POST'])
def index():
    return '''
    <p>Don't have an account? <a href="{{ url_for('routes.register') }}">Register here</a>.</p>
    if request.method == 'POST':
    
        from app.models import User

        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, email=email, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        flash('User registered successfully!', category='success')
        return redirect(url_for('routes.login'))

    return render_template('register.html')


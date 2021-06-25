from flask import Flask, render_template, redirect, url_for, flash, request
import os
import json
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_login import login_required, login_user, LoginManager, logout_user, current_user, UserMixin

with open('config.json') as c:
    params = json.load(c)["params"]

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET KEY'
app.config['UPLOAD_FOLDER'] = params['upload_location']
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/test_db_login'
db = SQLAlchemy(app)


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    type = db.Column(db.String(255), default="User")
    password = db.Column(db.String(255))
    profile_image = db.Column(db.String(255))


login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))


@app.route('/')
@login_required
def home():
    all_users = Users.query.order_by(Users.id)
    return render_template('home.html', user=current_user, all_users=all_users)


@app.route('/add-admin', methods=['POST', 'GET'])
@login_required
def add_admin():
    if request.method == 'POST':
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        user = Users.query.filter_by(email=email).first()

        if user:
            flash('An account with that email already exists!', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character', category='error')
        elif len(last_name) < 2:
            flash('Last name must be greater than 1 character', category='error')
        elif len(username) < 2:
            flash('Username must be greater than 1 character', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters', category='error')
        elif len(password) < 6:
            flash('Password must be at least 6 characters long', category='error')
        else:
            new_user = Users(first_name=first_name, last_name=last_name, username=username, email=email, type="Admin",
                             password=generate_password_hash(password, method='sha256'), profile_image="default")

            db.session.add(new_user)
            db.session.commit()
            flash('Admin added successfully!', category='success')
            return redirect(url_for('home'))
    return render_template('add-admin.html', user=current_user)


@app.route('/add-user', methods=['POST', 'GET'])
@login_required
def add_user():
    if request.method == 'POST':
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        user = Users.query.filter_by(email=email).first()

        if user:
            flash('An account with that email already exists!', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character', category='error')
        elif len(last_name) < 2:
            flash('Last name must be greater than 1 character', category='error')
        elif len(username) < 2:
            flash('Username must be greater than 1 character', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters', category='error')
        elif len(password) < 6:
            flash('Password must be at least 6 characters long', category='error')
        else:
            new_user = Users(first_name=first_name, last_name=last_name, username=username, email=email,
                             password=generate_password_hash(password, method='sha256'), profile_image="default")

            db.session.add(new_user)
            db.session.commit()
            flash('User added successfully!', category='success')
            return redirect(url_for('home'))

    return render_template('add-user.html', user=current_user)


@app.route('/profile', methods=['POST', 'GET'])
@login_required
def profile():
    if request.method == 'POST':
        profile_image = request.files['profileImage']
        image = secure_filename(profile_image.filename)

        if not profile_image:
            flash("Please select an image.", category='error')
        else:
            profile_image.save(os.path.join(app.config['UPLOAD_FOLDER'], image))
            user = Users.query.get_or_404(current_user.id)
            user.profile_image = image
            db.session.commit()
            return redirect(url_for('profile'))

    return render_template('profile.html', user=current_user)


@app.route('/super-users')
@login_required
def super_users():
    all_super_users = Users.query.order_by(Users.id)
    return render_template('super-users.html', user=current_user, all_super_users=all_super_users)


@app.route('/delete-user/<int:user_id>')
@login_required
def delete_user(user_id):
    user_to_delete = Users.query.get_or_404(user_id)
    db.session.delete(user_to_delete)
    db.session.commit()
    flash("User has been deleted.", category='success')
    return redirect(url_for('home'))


@app.route('/edit-user/<int:user_id>', methods=['POST', 'GET'])
@login_required
def edit_user(user_id):
    user_to_edit = Users.query.get_or_404(user_id)

    if request.method == 'POST':
        edited_first_name = request.form.get('firstName')
        edited_last_name = request.form.get('lastName')
        edited_username = request.form.get('username')

        if len(edited_first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif len(edited_last_name) < 2:
            flash('Last name must be greater than 1 character.', category='error')
        elif len(edited_username) < 1:
            flash('Username can\'t be empty.', category='error')
        else:
            user_to_edit.first_name = edited_first_name
            user_to_edit.last_name = edited_last_name
            user_to_edit.username = edited_username
            db.session.commit()
            flash('User information updated.', category='success')
            return redirect(url_for('home'))

    return render_template('edit-user.html', user=current_user, user_to_edit=user_to_edit)


@app.route('/demote-admin/<int:admin_id>')
@login_required
def demote_admin(admin_id):
    admin_to_demote = Users.query.get_or_404(admin_id)

    admin_to_demote.type = "User"
    db.session.commit()
    flash("Admin has been demoted.", category='success')
    return redirect(url_for('home'))


@app.route('/make-super/<int:id>')
@login_required
def make_super(id):
    user_to_make_super = Users.query.get_or_404(id)

    user_to_make_super.type = "Super"
    db.session.commit()
    flash("Selection has been promoted to super user.", category='success')
    return redirect(url_for('home'))


@app.route('/make-admin/<int:user_id>')
@login_required
def make_admin(user_id):
    user_to_make_admin = Users.query.get_or_404(user_id)

    user_to_make_admin.type = "Admin"
    db.session.commit()
    flash("User has been made admin.", category='success')
    return redirect(url_for('home'))


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        username = request.form.get('username')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        profile_image = request.files['profileImage']
        image = secure_filename(profile_image.filename)

        user = Users.query.filter_by(email=email).first()

        if user:
            flash("An account with this email already exists!", category='error')

        elif len(first_name) < 2:
            flash('First name must be greater than 1 character', category='error')
        elif len(last_name) < 2:
            flash('Last name must be greater than 1 character', category='error')
        elif len(username) < 2:
            flash('Username must be greater than 1 character', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters', category='error')
        elif len(password1) < 6:
            flash('Password must be at least 6 characters long', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        elif not profile_image:
            flash('Profile image cannot be empty', category='error')
        else:
            profile_image.save(os.path.join(app.config['UPLOAD_FOLDER'], image))
            new_user = Users(first_name=first_name, last_name=last_name, username=username, email=email,
                             password=generate_password_hash(password1, method='sha256'), profile_image=image)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully!', category='success')
            login_user(user, remember=True)
            return redirect(url_for('home'))

    return render_template('register.html', user=current_user)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = Users.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                flash(f'Logged in successfully! Welcome {current_user.first_name} {current_user.last_name}!', category='success')
                return redirect(url_for('home'))

            else:
                flash('Incorrect password! Try again', category='error')
        else:
            flash('Email does not exist.', category='error')
    return render_template('login.html', user=current_user)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)

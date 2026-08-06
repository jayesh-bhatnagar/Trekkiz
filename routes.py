from flask import render_template, redirect, request, session, url_for, flash
from models import db, Booking, User, Trek
from datetime import datetime, timedelta
from helpers import logged_in
from sqlalchemy import or_
from app import app

@app.route('/', methods = ['GET'])
def home():
    
    ''' This is the Home page landing route. '''
    return render_template('index.html')

@app.route('/signout', methods = ['GET'])
def logout():

    ''' This is the logging out route. '''
    session.clear()
    return redirect(url_for('home'))

@app.route('/register-success', methods = ['GET'])
def success():

    ''' This is the Registration success route. '''
    return render_template('success.html')

@app.route('/signup', methods = ['GET', 'POST'])
def register():

    ''' This is the Registration form route. '''
    if request.method == 'POST':
        user_name = request.form.get('u_name').strip()
        role = request.form.get('role')
        f_name = request.form.get('f_name')
        l_name = request.form.get('l_name')
        phone_number = request.form.get('contact').replace(' ', '').strip()

        if User.query.filter_by(user_name = user_name).first():
            flash(message = 'User name is already taken, kindly use another.', category = 'error')
            return render_template('register.html')
        if User.query.filter_by(phone_number = phone_number).first():
            flash(message = 'Phone number already exists. Use a different number.', category = 'error')
            return render_template('register.html')
        if len(phone_number) != 13:
            flash(message = 'Kindly enter a valid number.', category = 'error')
            return render_template('register.html')

        user = User(user_name = user_name, f_name = f_name, l_name = l_name, role = role, 
                    phone_number = phone_number)

        user.status = 'Approved' if user.role == 'trekker' else 'Pending'
        user.set_password(request.form.get('raw_password'))

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('success'))

    return render_template('register.html')

@app.route('/signin', methods = ['GET', 'POST'])
def login():

    ''' This is the Signin form route. '''
    if request.method == 'POST':

        session.clear()
        user_name = request.form.get('u_name').strip()
        password = request.form.get('password')

        user = User.query.filter_by(user_name = user_name).first()

        if user is None:
            flash('Invalid username or password', 'error')
            return redirect(url_for('login'))

        if not user.verify_password(password):
            flash('Invalid username or password', 'error')
            return redirect(url_for('login'))

        session['user_id'] = user.user_id
        session['role'] = user.role

        # if session.get('role') == 'staff':
        #     if user.status != 'Approved':
        #         return render_template('error.html', user = user)
        #     else:
        #         return redirect(url_for('staff_dash'))
        # elif session.get('role') == 'trekker':
        #     return redirect(url_for('trekker_dash'))
        # else:
        #     return redirect(url_for('admin_dash'))

    return render_template('signin.html')


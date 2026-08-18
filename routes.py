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
    if logged_in():
        session.clear()
    return redirect(url_for('home'))

@app.route('/register-success', methods = ['GET'])
def success():

    ''' This is the Registration success route. '''
    return render_template('auth-success.html')

@app.route('/signup', methods = ['GET', 'POST'])
def register():

    ''' This is the Registration form route. '''
    if request.method == 'POST':
        user_name = request.form.get('u_name').strip()
        role = request.form.get('role')
        f_name = request.form.get('f_name').strip()
        l_name = request.form.get('l_name').strip()
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
        user.set_password(request.form.get('raw_password').strip())

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
        password = request.form.get('password').strip()

        user = User.query.filter_by(user_name = user_name).first()

        if user is None:
            flash('Invalid username or password', 'error')
            return redirect(url_for('login'))
        if not user.verify_password(password):
            flash('Invalid username or password', 'error')
            return redirect(url_for('login'))

        session['user_id'] = user.user_id
        session['role'] = user.role

        if session.get('role') == 'staff':
            if user.status != 'Approved':
                return render_template('auth-error.html', user = user)
            else:
                return redirect(url_for('staff_dash'))
        elif session.get('role') == 'trekker':
            return redirect(url_for('trekker_dash'))
        else:
            return redirect(url_for('admin_dash'))

    return render_template('signin.html')

@app.route('/admin-dash', methods = ['GET'])
def admin_dash():
    if session.get('role') != 'admin':
        return redirect(url_for('home'))
    admin = logged_in()

    all_treks = Trek.query.all()
    guides = User.query.filter_by(role = 'staff', status = 'Approved').all()
    trekkers = User.query.filter_by(role = 'trekker').all()
    bookings = Booking.query.all()

    treks = Trek.query.limit(5).all()
    pending_staff = User.query.filter_by(role = 'staff', status = 'Pending').limit(5).all()
    request_count = User.query.filter_by(role = 'staff', status = 'Pending').count()

    search_query = request.args.get('query', '').strip()
    search_result_treks = []
    search_result_users = []

    if search_query:
        like = f'%{search_query}%'
        search_result_treks = Trek.query.filter(or_(Trek.name.like(like), Trek.difficulty.like(like),
                                                    Trek.location.like(like), Trek.status.like(like))).all()
        search_result_users = User.query.filter(or_(User.f_name.like(like), User.l_name.like(like), 
                                                     User.role.like(like), User.status.like(like))).all()
    
    return render_template('admin-dash.html', user = admin, guides = guides, treks = treks, requests = request_count,
                           all_treks = all_treks, trekkers = trekkers, bookings = bookings, pending_staff = pending_staff,
                           treks_found = search_result_treks, users_found = search_result_users, query = search_query)

@app.route('/admin-dash/approve-staff/<int:staff_id>', methods = ['POST'])
def approve_staff(staff_id):
    if session.get('role') != 'admin':
        return redirect(url_for('home'))
    guide = User.query.get(staff_id)
    guide.status = 'Approved'
    db.session.commit()
    return redirect(url_for('admin_dash'))

@app.route('/admin-dash/reject-staff/<int:staff_id>', methods = ['POST'])
def reject_staff(staff_id):
    if session.get('role') != 'admin':
        return redirect(url_for('home'))
    guide = User.query.get(staff_id)
    guide.status = 'Rejected'
    db.session.commit()
    return redirect(url_for('admin_dash'))

@app.route('/admin-dash/blacklist/<int:user_id>', methods = ['POST'])
def blacklist(user_id):
    if session.get('role') != 'admin':
        return redirect(url_for('home'))
    user = User.query.get(user_id)
    user.status = 'Blacklisted'
    user.isBlackListed = True
    db.session.commit()
    return redirect(url_for('admin_dash'))

@app.route('/admin-dash/unblacklist/<int:user_id>', methods = ['POST'])
def unblacklist(user_id):
    if session.get('role') != 'admin':
        return redirect(url_for('home'))
    user = User.query.get(user_id)
    user.status = 'Approved'
    user.isBlackListed = False
    db.session.commit()
    return redirect(url_for('admin_dash'))
    

@app.route('/staff-dash', methods = ['GET', 'POST'])
def staff_dash():
    if session.get('role') != 'staff':
        return redirect(url_for('home'))
    guide = logged_in()
    return render_template('staff-dash.html', user = guide)

@app.route('/trekker-dash', methods = ['GET', 'POST'])
def trekker_dash():
    if session.get('role') != 'trekker':
        return redirect(url_for('home'))
    trekker = logged_in()
    return render_template('user-dash.html', user = trekker)
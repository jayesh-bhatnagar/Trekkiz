from models import Users, db
from flask import session

def create_admin():

    if not Users.query.filter_by(role = 'admin').first():
        admin = Users(role = 'admin', user_name = 'trek-admin', status = 'Approved',
                      f_name = 'Administrator', isBlackListed = False)
        admin.set_password('123456')
        db.session.add(admin)
        db.session.commit()

def logged_in():

    user_id = session.get('user_id')
    if user_id:
        return Users.query.get_or_404(user_id)
    return None
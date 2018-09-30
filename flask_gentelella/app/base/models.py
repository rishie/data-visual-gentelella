from bcrypt import gensalt, hashpw
from flask_login import UserMixin

from app import login_manager

# can add graphQL model here


# @login_manager.user_loader
def user_loader(id):
    return User.query.filter_by(id=id).first()


# @login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    user = User.query.filter_by(username=username).first()
    return user if user else None

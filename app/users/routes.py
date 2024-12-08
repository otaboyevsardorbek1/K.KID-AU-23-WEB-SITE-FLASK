from flask import Blueprint, render_template

users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('/index')
def index():
    return render_template('users/index.html')

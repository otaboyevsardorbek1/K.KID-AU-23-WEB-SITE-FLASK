from flask import Blueprint, render_template

admins_bp = Blueprint('admins', __name__, url_prefix='/admins')

@admins_bp.route('/index')
def index():
    return render_template('admins/index.html')

from flask import Blueprint, render_template

owners_bp = Blueprint('owners', __name__, url_prefix='/owners')

@owners_bp.route('/index')
def index():
    return render_template('owners/index.html')

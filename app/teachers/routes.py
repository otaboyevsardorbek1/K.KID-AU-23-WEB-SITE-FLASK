from flask import Blueprint, render_template

teachers_bp = Blueprint('teachers', __name__, url_prefix='/teachers')

@teachers_bp.route('/index')
def index():
    return render_template('teachers/index.html')

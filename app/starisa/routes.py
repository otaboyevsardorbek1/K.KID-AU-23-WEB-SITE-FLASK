from flask import Blueprint, render_template

starisa_bp = Blueprint('starisa', __name__, url_prefix='/starisa')

@starisa_bp.route('/index')
def index():
    return render_template('starisa/index.html')

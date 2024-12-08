from flask import Blueprint, render_template

kuratr_bp = Blueprint('kuratr', __name__, url_prefix='/kuratr')

@kuratr_bp.route('/index')
def index():
    return render_template('kuratr/index.html')

from flask import Flask, render_template, redirect, url_for, session, flash,request
from app.users.routes import users_bp
from app.admins.routes import admins_bp
from app.teachers.routes import teachers_bp
from app.owners.routes import owners_bp
from app.starisa.routes import starisa_bp
from app.kuratr.routes import kuratr_bp
from middleware import block_bots

app = Flask(__name__)
app.secret_key = 'hggygyt56f7r6r'

# Botlarni har doim tekshir
block_bots(app)
# Blueprintlarni ro�yxatga olish
app.register_blueprint(users_bp)
app.register_blueprint(admins_bp)
app.register_blueprint(teachers_bp)
app.register_blueprint(owners_bp)
app.register_blueprint(starisa_bp)
app.register_blueprint(kuratr_bp)

# Login sahifasi
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        role = request.form.get('role')  # foydalanuvchi rolini olish
        if role:
            session['role'] = role
            return redirect(url_for(f'{role}.index'))  # ro'lga mos sahifaga yo'naltirish
        flash("Rolni tanlang!", "error")
    return render_template('login.html')

# Logout funksiyasi
@app.route('/logout')
def logout():
    session.pop('role', None)
    flash("You have logged out successfully", "success")
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

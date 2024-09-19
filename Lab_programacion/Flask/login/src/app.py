from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

from config import config

# Modelos
#from models.User import User    

#Formularios
#from forms.login import LoginForm


app = Flask(__name__)
app.config.from_object(config['development'])

db = SQLAlchemy(app)
login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, username, password):
        self.username = username    
        self.password = generate_password_hash(password)

    def check_password(self, pwd):
        return check_password_hash(self.password, pwd)




class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(max=100)])
    password = PasswordField('password', validators=[DataRequired(), Length(min=5, max=100)])
    submit = SubmitField('Sign in')





@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        
        if user and user.check_password(form.password.data):
            # Si las credenciales son correctas, inicia la sesión
            login_user(user)
            flash('Has iniciado sesión con éxito', 'success')
            return redirect(url_for('home'))  # Redirige a la página de inicio o dashboard
        else:
            flash('Correo o contraseña incorrectos', 'danger')
            render_template('auth/login.html', form=form)
    
    return render_template('auth/login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/protected')
@login_required
def protected():
    return "<h1>Esta es una vista protegida, solo para usuarios autenticados.</h1>"


def status_401(error):
    return redirect(url_for('login'))


def status_404(error):
    return "<h1>Página no encontrada</h1>", 404


app.register_error_handler(401, status_401)
app.register_error_handler(404, status_404)



with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()

import flask
from config import *

app = Flask(__name__)

conexion = MySQL(app)

ingreso = flask.Blueprint('ingreso',__name__)

@ingreso.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        usuario = User(0,request.form['username'],request.form['password'])
        usuario_logueado = ModelUser.login(conexion, usuario)
        if usuario_logueado != None:
            if usuario_logueado.password:
                if usuario_logueado.estado_usuario == 1:
                    login_user(usuario_logueado)
                    return redirect(url_for('presentacion'))
                else:
                    flash('Usuario Inactivo')
                    data = { 'titulo': 'Inicio de Sesión' }
                    return render_template('auth/login.html',data=data)
            else:
                flash('Contraseña incorrecta')
                data = { 'titulo': 'Inicio de Sesión' }
                return render_template('auth/login.html',data=data)
        else:
            flash('El usuario no existe')
            data = { 'titulo': 'Inicio de Sesión' }
            return render_template('auth/login.html',data=data)
    else:
        data = { 'titulo': 'Inicio de Sesión' }
        return render_template('auth/login.html',data=data)

@ingreso.route('/logout')
def cerrar_sesion():
    logout_user()
    return redirect(url_for('ingreso.login'))
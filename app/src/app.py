import re
from flask_login import LoginManager, current_user
from config import *
# Date
import datetime
from routes.listados_routes import listados
from routes.login_routes import ingreso
from routes.editar_perfil_routes import edicion_perfil
from routes.admin_usuarios import admin_usuarios
from routes.gestion_docs_routes import gestion_docs

app = Flask(__name__)

conexion = MySQL(app)

csrf = CSRFProtect()

login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.obtener_usuario(conexion,id)


@app.route('/')
def index():
    if User:
        return redirect(url_for('presentacion'))
    else:
        return redirect(url_for('ingreso.login'))

@app.route('/home')
@login_required
def presentacion():
    data = { 'titulo': 'Inicio' }
    return render_template('presentacion.html',data=data)

#---------- Blueprints -----------

app.register_blueprint(listados)
app.register_blueprint(ingreso)
app.register_blueprint(edicion_perfil)
app.register_blueprint(admin_usuarios)
app.register_blueprint(gestion_docs)

#---------- EndBlueprints --------

@app.context_processor
def inject_today_date():
    return {'hoy': datetime.date.today()}

def pagina_no_encontrada(error):
    return render_template('error.html'),404

def pagina_protegida(error):
    return redirect(url_for('ingreso.login'))

if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(404, pagina_no_encontrada)
    app.register_error_handler(401, pagina_protegida)
    app.run()
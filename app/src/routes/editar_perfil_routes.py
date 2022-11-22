import flask
from config import *
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

conexion = MySQL(app)

edicion_perfil = flask.Blueprint('editar_perfil',__name__)

@edicion_perfil.route('/editar_perfil')
@login_required
def editar_perfil():
    data = { 'titulo':'Editar Perfil' }
    return render_template('editar_perfil.html',data=data)

@edicion_perfil.route('/editar/perfil/<id>', methods=['POST'])
@login_required
def editando_perfil(id):
    if request.method == 'POST':
        try:
            cursor = conexion.connection.cursor()
            sql = """UPDATE usuario SET nombre_usuario = '{0}', correo_usuario = '{1}', telefono_usuario = '{2}' 
                    WHERE idusuario = '{3}'""".format(request.form['nombre_usuario'],request.form['correo_usuario'], request.form['telefono_usuario'],id)
            cursor.execute(sql)        
            conexion.connection.commit()
            flash('Perfil Actualizado Correctamente')
            return redirect(url_for('editar_perfil.editar_perfil'))
        except Exception as ex:
            flash('Error...','error')
            return redirect(url_for('editar_perfil.editar_perfil'))
    else:
        return redirect(url_for('editar_perfil.editar_perfil'))

@edicion_perfil.route('/cambiar_pass')
@login_required
def editar_pass():
    data = { 'titulo':'Cambiar Contraseña' }
    return render_template('cambiar_pass.html',data=data)

@edicion_perfil.route('/editar/pass/<id>', methods=['POST'])
@login_required
def editando_pass(id):
    if request.method == 'POST':
        actual = request.form['actual']
        nueva = request.form['nueva_pass']
        repeticion = request.form['repeticion']
        if check_password_hash(current_user.password,actual):
            if nueva == repeticion:
                if actual != nueva:
                    nueva_pass = generate_password_hash(nueva)
                    try:
                        cursor = conexion.connection.cursor()
                        sql = """UPDATE usuario SET password = '{0}' 
                                WHERE idusuario = '{1}'""".format(nueva_pass,id)
                        cursor.execute(sql)        
                        conexion.connection.commit()
                        flash('Contraseña Cambiada Correctamente. Por favor, vuelva a iniciar sesión.')
                        return redirect(url_for('editar_perfil.editar_pass'))
                    except Exception as ex:
                        flash('Error...','error')
                        return redirect(url_for('editar_perfil.editar_pass'))
                else:
                    flash('La nueva contraseña no puede ser igual a la anterior','error')
                    return redirect(url_for('editar_perfil.editar_pass'))
            else:
                flash('Las contraseñas ingresadas no coinciden','error')
                return redirect(url_for('editar_perfil.editar_pass'))
        else:
            flash('Contraseña actual incorrecta','error')
            return redirect(url_for('editar_perfil.editar_pass'))  
    else:
        return redirect(url_for('editar_perfil.editar_pass'))
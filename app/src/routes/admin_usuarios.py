import flask
from config import *
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

conexion = MySQL(app)

admin_usuarios = flask.Blueprint('admin_usuarios',__name__)

@admin_usuarios.route('/crear_usuario')
@login_required
def crear_usuario():
    data = { 'titulo':'Crear Usuarios Nuevos' }
    if current_user.rol_usuario == 1:
        return render_template('crear_usuario.html',data=data)
    else:
        return redirect(url_for('index'))


@admin_usuarios.route('/crear/usuario', methods=['POST'])
@login_required
def creando_usuario():
    if current_user.rol_usuario == 1:
        if request.method == 'POST':
            username = request.form['username']
            password = generate_password_hash(request.form['password'])
            nu = request.form['nombre_usuario']
            nombre_usuario = nu.replace("'","")
            cu = request.form['correo_usuario']
            correo_usuario = cu.replace("'","")
            telefono_usuario = request.form['telefono_usuario']
            estado_usuario = request.form['estado_usuario']
            rol_usuario = request.form['rol_usuario']
            try:
                cursor = conexion.connection.cursor()
                sql = """INSERT INTO usuario(username, password, nombre_usuario, correo_usuario, telefono_usuario, estado_usuario, rol_usuario) 
                        VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}') """.format(username, password, nombre_usuario, correo_usuario, telefono_usuario, estado_usuario, rol_usuario)
                cursor.execute(sql)        
                conexion.connection.commit()
                flash('Usuario Creado Correctamente')
                return redirect(url_for('admin_usuarios.crear_usuario'))
            except Exception as ex:
                flash('Error...','error')
                return redirect(url_for('admin_usuarios.crear_usuario'))
        else:
            return redirect(url_for('admin_usuarios.crear_usuario'))
    else:
        return redirect(url_for('index'))


@admin_usuarios.route('/lista_usuarios')
@login_required
def listado_usuarios():
    if current_user.rol_usuario == 1:
        cursor = conexion.connection.cursor()
        sql = """SELECT idusuario, username, nombre_usuario, correo_usuario, telefono_usuario, IF(estado_usuario=1,"Activo","Inactivo") as estado_usuario, IF(rol_usuario=1,"Administrador","Consultante") as rol_usuario 
                FROM usuario"""
        cursor.execute(sql)
        usuarios = cursor.fetchall()
        if usuarios:
            registro = usuarios[0]
        else:
            registro = ''
        data = { 'titulo': 'Usuarios Registrados',
                'encabezado': registro }
        return render_template('listado_usuarios.html',data=data, usuarios=usuarios)
    else:
        return redirect(url_for('index'))

@admin_usuarios.route('/lista_usuarios/search', methods=['POST', 'GET'])
@login_required
def listado_usuarios_search():
    if current_user.rol_usuario == 1:
        if request.method == 'POST':
            b = request.form['search_input']
            busqueda = b.replace("'","")
            cursor = conexion.connection.cursor()
            sql = """SELECT idusuario, username, nombre_usuario, correo_usuario, telefono_usuario, IF(estado_usuario=1,"Activo","Inactivo") as estado_usuario, IF(rol_usuario=1,"Administrador","Consultante") as rol_usuario 
                    FROM usuario
                    WHERE CONCAT(username,' ', nombre_usuario,' ',IF(estado_usuario=1,"Activo","Inactivo"),' ',IF(rol_usuario=1,"Administrador","Consultante")) LIKE '%{0}%'""".format(busqueda)
            cursor.execute(sql)
            usuarios = cursor.fetchall()
            if usuarios:
                registro = usuarios[0]
            else:
                registro = ''
            data = { 'titulo': 'Usuarios Registrados',
                    'encabezado': registro,
                    'busqueda': busqueda }
            return render_template('listado_usuarios.html',data=data, usuarios=usuarios)
        else:
            return redirect(url_for('admin_usuarios.listado_usuarios'))

    else:
        return redirect(url_for('index'))

@admin_usuarios.route('/cambiar_rol/<id>/<rol>')
@login_required
def cambiar_rol(id,rol):
    if current_user.rol_usuario == 1:
        if rol == 'Administrador':
            nuevo_rol = '2'
        else:
            nuevo_rol = '1'
        try:
            cursor = conexion.connection.cursor()
            sql = """UPDATE usuario SET rol_usuario = '{0}' 
                     WHERE idusuario = '{1}'""".format(nuevo_rol,id)
            cursor.execute(sql)        
            conexion.connection.commit()
            flash('El Rol del usuario ha sido cambiado correctamente')
            return redirect(url_for('admin_usuarios.listado_usuarios'))
        except Exception as ex:
            flash('Error...','error')
            return redirect(url_for('admin_usuarios.listado_usuarios'))
    else:
        return redirect(url_for('index'))

@admin_usuarios.route('/cambiar_estado/<id>/<estado>')
@login_required
def cambiar_estado(id,estado):
    if current_user.rol_usuario == 1:
        if estado == 'Activo':
            nuevo_estado = '0'
        else:
            nuevo_estado = '1'
        try:
            cursor = conexion.connection.cursor()
            sql = """UPDATE usuario SET estado_usuario = '{0}' 
                     WHERE idusuario = '{1}'""".format(nuevo_estado,id)
            cursor.execute(sql)        
            conexion.connection.commit()
            flash('El Estado del usuario ha sido cambiado correctamente')
            return redirect(url_for('admin_usuarios.listado_usuarios'))
        except Exception as ex:
            flash('Error...','error')
            return redirect(url_for('admin_usuarios.listado_usuarios'))
    else:
        return redirect(url_for('index'))

@admin_usuarios.route('/eliminar_usuario/<id>/<est>/<rol>')
@login_required
def eliminar_usuario(id,est,rol):
    if current_user.rol_usuario == 1:
        if est == 'Activo' or rol == 'Administrador':
            flash('No se puede eliminar un usuario activo o con rol de administrador','error')
            return redirect(url_for('admin_usuarios.listado_usuarios'))
        else:
            try:
                cursor = conexion.connection.cursor()
                sql = """DELETE FROM usuario 
                        WHERE idusuario = '{0}'""".format(id)
                cursor.execute(sql)        
                conexion.connection.commit()
                flash('Usuario Eliminado Correctamente')
                return redirect(url_for('admin_usuarios.listado_usuarios'))
            except Exception as ex:
                flash('Error...','error')
                return redirect(url_for('admin_usuarios.listado_usuarios'))
    else:
        return redirect(url_for('index'))
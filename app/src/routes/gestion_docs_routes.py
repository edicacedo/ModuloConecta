from ast import For
from codecs import ignore_errors
from fileinput import filename
import flask
from config import *

app = Flask(__name__)

conexion = MySQL(app)

gestion_docs = flask.Blueprint('gestion_docs',__name__)

def obtener_carpetas():
        cursor = conexion.connection.cursor()
        sql = "SELECT idcarpeta, nombre_carpeta FROM carpeta"
        cursor.execute(sql)
        carpetas = cursor.fetchall()
        return carpetas

def buscando(busqueda,carpeta,subcarpeta):
    cursor = conexion.connection.cursor()
    if busqueda == '' and subcarpeta == '':
        sql = """SELECT d.iddocumento, c.nombre_carpeta, s.nombre_subcarpeta, d.nombre_documento, d.fecha_documento, d.version_documento, c.idcarpeta, s.idsubcarpeta, d.estado_documento 
                 FROM documento d, carpeta c, subcarpeta s 
                 WHERE d.carpeta = c.idcarpeta AND d.subcarpeta = s.idsubcarpeta AND c.idcarpeta = s.carpeta_id 
                 AND d.carpeta = '{0}' 
                 ORDER BY d.nombre_documento ASC""".format(carpeta)
        cursor.execute(sql)
        docs = cursor.fetchall()
        data = { 'titulo':'Actualizar Documento/Formato',
                 }
        carp = obtener_carpetas()
        if not docs:
            flash('No se encontraron resultados para la busqueda.','error')
            
    elif busqueda == '' and carpeta != '' and subcarpeta != '':
        sql = """SELECT d.iddocumento, c.nombre_carpeta, s.nombre_subcarpeta, d.nombre_documento, d.fecha_documento, d.version_documento, c.idcarpeta, s.idsubcarpeta, d.estado_documento 
                 FROM documento d, carpeta c, subcarpeta s 
                 WHERE d.carpeta = c.idcarpeta AND d.subcarpeta = s.idsubcarpeta AND c.idcarpeta = s.carpeta_id 
                 AND d.carpeta = '{0}' AND s.idsubcarpeta = '{1}'
                 ORDER BY d.nombre_documento ASC""".format(carpeta, subcarpeta)
        cursor.execute(sql)
        docs = cursor.fetchall()
        data = { 'titulo':'Actualizar Documento/Formato',
                 }
        carp = obtener_carpetas()
        if not docs:
            flash('No se encontraron resultados para la busqueda.','error')
           
    else:
        sql = """SELECT d.iddocumento, c.nombre_carpeta, s.nombre_subcarpeta, d.nombre_documento, d.fecha_documento, d.version_documento, c.idcarpeta, s.idsubcarpeta, d.estado_documento 
                 FROM documento d, carpeta c, subcarpeta s 
                 WHERE d.carpeta = c.idcarpeta AND d.subcarpeta = s.idsubcarpeta AND c.idcarpeta = s.carpeta_id 
                 AND CONCAT(d.nombre_documento,' ',c.nombre_carpeta,' ',s.nombre_subcarpeta,' ',date_format(d.fecha_documento, "%d/%m/%Y")) LIKE '%{0}%'
                 ORDER BY d.nombre_documento ASC""".format(busqueda)
        cursor.execute(sql)
        docs = cursor.fetchall()
        data = { 'titulo':'Actualizar Documento/Formato',
                 'busqueda': busqueda
               }
        carp = obtener_carpetas()
        if not docs:
            flash('No se encontraron resultados para la busqueda.','error')
    
    res = {'data':data, 'carp': carp, 'docs':docs} 
    return res

@gestion_docs.route('/subir_doc')
@login_required
def subir_doc():
    data = { 'titulo':'Subir Documento/Formato' }
    if current_user.rol_usuario == 1:
        carpetas = obtener_carpetas()

        return render_template('subir_doc.html',data=data, carpetas=carpetas)
    else:
        return redirect(url_for('index'))

@gestion_docs.route('/subcarpeta/<id>')
@login_required
def sub_por_carpeta(id):
    if current_user.rol_usuario == 1:
        cursor = conexion.connection.cursor()
        sql = """SELECT idsubcarpeta, carpeta_id, nombre_subcarpeta 
                FROM subcarpeta 
                WHERE carpeta_id = '{0}'""".format(id)
        cursor.execute(sql)
        subcarpetas = cursor.fetchall()
        subcarpetasArray = []
        for subcarpeta in subcarpetas:
            subcarpetaObj = {
                'id': subcarpeta[0],
                'nombre': subcarpeta[2] 
            }
            subcarpetasArray.append(subcarpetaObj)
        return jsonify({'subprocesos':subcarpetasArray})

    else:
        return redirect(url_for('index'))


@gestion_docs.route('/editar_docs/subcarpeta/<id>')
@login_required
def subcarp_por_carpeta(id):
    if current_user.rol_usuario == 1:
        cursor = conexion.connection.cursor()
        sql = """SELECT idsubcarpeta, carpeta_id, nombre_subcarpeta 
                FROM subcarpeta 
                WHERE carpeta_id = '{0}'""".format(id)
        cursor.execute(sql)
        subcarpetas = cursor.fetchall()
        subcarpetasArray = []
        for subcarpeta in subcarpetas:
            subcarpetaObj = {
                'id': subcarpeta[0],
                'nombre': subcarpeta[2] 
            }
            subcarpetasArray.append(subcarpetaObj)
        return jsonify({'subprocesos':subcarpetasArray})

    else:
        return redirect(url_for('index'))



@gestion_docs.route('/subir/archivo', methods=['POST'])
@login_required
def subiendo_archivo():
    data = { 'titulo':'Subir Documento/Formato' }
    if current_user.rol_usuario == 1:
        if request.method == 'POST':
            carpeta = request.form['select_carpeta']
            subcarpeta = request.form['select_subcarpeta']
            fecha = request.form['fecha_archivo']
            estado = request.form['select_estado']

            try:
                path = Path('src/static/archivos/'+carpeta+'/'+subcarpeta)
                path.mkdir(parents=True)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
            
            f = request.files['archivo']
            filename = secure_filename(f.filename)
            basedir = os.path.abspath(os.path.dirname(__file__))

            f.save(os.path.join(basedir, '../../src/static/archivos/'+carpeta+'/'+subcarpeta, filename))
            
            cursor = conexion.connection.cursor()
            sql = """INSERT INTO documento(carpeta, subcarpeta, nombre_documento, fecha_documento, version_documento, estado_documento)
                    VALUES (%s, %s, %s, %s, '1' ,%s) """
            cursor.execute(sql,(carpeta, subcarpeta, filename, fecha, estado))
            conexion.connection.commit()
            flash('Documento Agregado Correctamente')
            return redirect(url_for('gestion_docs.subir_doc'))
    else:
        return redirect(url_for('index'))

@gestion_docs.route('/actualizar')
@login_required
def actualizar_doc():
    data = { 'titulo':'Actualizar Documento/Formato' }
    if current_user.rol_usuario == 1:
        carpetas = obtener_carpetas()
        return render_template('listado_docs.html',data=data, carpetas=carpetas)
    else:
        return redirect(url_for('index'))

@gestion_docs.route('/actualizar', methods=['POST'])
@login_required
def buscar_docs():
    if current_user.rol_usuario == 1:
        if request.method == 'POST':
            carpeta = request.form['select_carpeta']
            subcarpeta = request.form['select_subcarpeta']
            b = request.form['search_input']
            busqueda = b.replace("'","")
            res = buscando(busqueda,carpeta,subcarpeta)
            return render_template('listado_docs.html',data=res['data'], carpetas=res['carp'], docs=res['docs'])
    
    else:
        return redirect(url_for('index'))

@gestion_docs.route('/eliminar_documento/<id>/<carpeta>/<subcarpeta>/<archivo>')
@login_required
def eliminar_usuario(id,carpeta,subcarpeta, archivo):
    if current_user.rol_usuario == 1:
        try:
            remove('src/static/archivos/'+carpeta+"/"+subcarpeta+"/"+archivo)
            
            cursor = conexion.connection.cursor()
            sql = """DELETE FROM documento 
                     WHERE iddocumento = '{0}'""".format(id)
            cursor.execute(sql)        
            conexion.connection.commit()
            flash('Documento Eliminado Correctamente')
            return redirect(url_for('gestion_docs.actualizar_doc'))
        except Exception as ex:
            flash('Error...','error')
            return redirect(url_for('gestion_docs.actualizar_doc'))
    else:
        return redirect(url_for('index'))

@gestion_docs.route('/editar_docs/<id>')
@login_required
def editar_docs(id):
    data = { 'titulo':'Actualizar Documento/Formato' }
    if current_user.rol_usuario == 1:
        cursor = conexion.connection.cursor()
        sql = """SELECT d.iddocumento, c.nombre_carpeta, s.nombre_subcarpeta, d.nombre_documento, d.fecha_documento, d.version_documento, c.idcarpeta, s.idsubcarpeta, d.estado_documento
                 FROM documento d, carpeta c, subcarpeta s 
                 WHERE d.carpeta = c.idcarpeta AND d.subcarpeta = s.idsubcarpeta AND c.idcarpeta = s.carpeta_id 
                 AND d.iddocumento = '{0}'""".format(id)
        cursor.execute(sql)
        documento = cursor.fetchone()
        carpetas = obtener_carpetas()

        return render_template('editar_docs.html',data=data, documento=documento, carpetas=carpetas)
    else:
        return redirect(url_for('index'))


@gestion_docs.route('/editar/archivo/<id>/<carp>/<sub>/<arch>', methods=['POST'])
@login_required
def editando_doc(id, carp, sub, arch):
    data = { 'titulo':'Actualizar Documento/Formato' }
    if current_user.rol_usuario == 1:
        if request.method == 'POST':
            
            carpeta = request.form['select_carpeta']
            subcarpeta = request.form['select_subcarpeta']
            f = request.files['archivo']
            filename = secure_filename(f.filename)
            fecha = request.form['fecha_archivo']
            estado = request.form['select_estado']
            version = request.form['version']

            conjunto = []
            if carpeta and subcarpeta:
                conjunto.append("carpeta = '{0}', subcarpeta = '{1}'".format(carpeta,subcarpeta))
            if f:
                nueva_version = int(version)+1
                conjunto.append("nombre_documento = '{0}', version_documento = '{1}'".format(filename,nueva_version))
                
                try:
                    remove('src/static/archivos/'+carp+"/"+sub+"/"+arch)
                except OSError as e:
                    if e.errno != errno.EEXIST:
                        ignore_errors
                
                try:
                    path = Path('src/static/archivos/'+carp+'/'+sub)
                    path.mkdir(parents=True)
                except OSError as e:
                    if e.errno != errno.EEXIST:
                        raise
                basedir = os.path.abspath(os.path.dirname(__file__))
                f.save(os.path.join(basedir, '../../src/static/archivos/'+carp+'/'+sub, filename))
            
            if fecha:
                conjunto.append("fecha_documento = '{0}'".format(fecha))
            if estado:
                conjunto.append("estado_documento = '{0}'".format(estado))
        
            datos_consulta = ' , '.join(map(str,conjunto))

            cursor = conexion.connection.cursor()
            sql = """UPDATE documento SET {0}
                     WHERE iddocumento = '{1}'""".format(datos_consulta,id)
            cursor.execute(sql)        
            conexion.connection.commit()
            flash('Documento Actualizado Correctamente')
            
            return redirect(url_for('gestion_docs.editar_docs', id=id))
    else:
        return redirect(url_for('index'))

@gestion_docs.route('/historial')
@login_required
def historial_docs():
    data = { 'titulo':'Historial de Cambios' }
    if current_user.rol_usuario == 1:
        carpetas = obtener_carpetas()
        return render_template('historial_docs.html',data=data, carpetas=carpetas)
    else:
        return redirect(url_for('index'))

@gestion_docs.route('/historial', methods=['POST'])
@login_required
def busqueda_historial():
    if current_user.rol_usuario == 1:
        if request.method == 'POST':
            carpeta = request.form['select_carpeta']
            subcarpeta = request.form['select_subcarpeta']
            b = request.form['search_input']
            busqueda = b.replace("'","")
            res = buscando(busqueda,carpeta,subcarpeta)
            
            cursor = conexion.connection.cursor()
            sql = """SELECT h.idhist_documento, h.documento_id, c.nombre_carpeta, s.nombre_subcarpeta, h.nombre_documento, h.fecha_documento, h.version_documento, IF(h.estado_documento = 1, 'Activo', 'Inactivo') as estado, h.fecha_cambio
                     FROM historial_documento h, carpeta c, subcarpeta s 
                     WHERE h.carpeta = c.idcarpeta AND h.subcarpeta = s.idsubcarpeta
                     ORDER BY h.fecha_cambio DESC"""
            cursor.execute(sql)
            cambios = cursor.fetchall()


            return render_template('historial_docs.html',data=res['data'], carpetas=res['carp'], docs=res['docs'], cambios=cambios)
    
    else:
        return redirect(url_for('index'))
import flask
from config import *

app = Flask(__name__)

conexion = MySQL(app)

listados = flask.Blueprint('listados',__name__)

# ------------------ Rutas Listado ----------------------
@listados.route('/listado/<carpeta>')
@login_required
def lista(carpeta):
    cursor = conexion.connection.cursor()
    sql = """SELECT d.iddocumento, c.nombre_carpeta, s.nombre_subcarpeta, d.nombre_documento, d.fecha_documento, d.version_documento, c.idcarpeta, s.idsubcarpeta, d.estado_documento 
            FROM documento d, carpeta c, subcarpeta s 
            WHERE d.carpeta = c.idcarpeta AND d.subcarpeta = s.idsubcarpeta AND c.idcarpeta = s.carpeta_id AND d.estado_documento = 1 AND c.idcarpeta = '{0}'
            ORDER BY d.iddocumento DESC""".format(carpeta)
    cursor.execute(sql)
    docs = cursor.fetchall()
    if docs:
        registro = docs[0]
    else:
        registro = ''

    data = { 'titulo': 'Formatos Encontrados',
            'encabezado': registro }
    return render_template('listado.html',data=data, docs=docs)

@listados.route('/listado/sub/<subcarpeta>')
@login_required
def lista_sub(subcarpeta):
    cursor = conexion.connection.cursor()
    sql = """SELECT d.iddocumento, c.nombre_carpeta, s.nombre_subcarpeta, d.nombre_documento, d.fecha_documento, d.version_documento, c.idcarpeta, s.idsubcarpeta, d.estado_documento 
            FROM documento d, carpeta c, subcarpeta s 
            WHERE d.carpeta = c.idcarpeta AND d.subcarpeta = s.idsubcarpeta AND c.idcarpeta = s.carpeta_id AND d.estado_documento = 1 AND s.idsubcarpeta = '{0}'
            ORDER BY d.iddocumento DESC""".format(subcarpeta)
    cursor.execute(sql)
    docs = cursor.fetchall()
    if docs:
        registro = docs[0]
    else:
        registro = ''
    data = { 'titulo': 'Formatos Encontrados',
            'encabezado': registro,
            'sub': True
            }
    return render_template('listado.html',data=data, docs=docs)

@listados.route('/listado/sort/file/<carpeta>')
@login_required
def lista_sort_file(carpeta):
    cursor = conexion.connection.cursor()
    sql = """SELECT d.iddocumento, c.nombre_carpeta, s.nombre_subcarpeta, d.nombre_documento, d.fecha_documento, d.version_documento, c.idcarpeta, s.idsubcarpeta, d.estado_documento 
            FROM documento d, carpeta c, subcarpeta s 
            WHERE d.carpeta = c.idcarpeta AND d.subcarpeta = s.idsubcarpeta AND c.idcarpeta = s.carpeta_id AND d.estado_documento = 1 AND c.idcarpeta = '{0}'
            ORDER BY d.nombre_documento ASC""".format(carpeta)
    cursor.execute(sql)
    docs = cursor.fetchall()
    if docs:
        registro = docs[0]
    else:
        registro = ''
    data = { 'titulo': 'Formatos Encontrados',
            'encabezado': registro
            }
    return render_template('listado.html',data=data, docs=docs)

@listados.route('/listado/sort/date/<carpeta>')
@login_required
def lista_sort_date(carpeta):
    cursor = conexion.connection.cursor()
    sql = """SELECT d.iddocumento, c.nombre_carpeta, s.nombre_subcarpeta, d.nombre_documento, d.fecha_documento, d.version_documento, c.idcarpeta, s.idsubcarpeta, d.estado_documento 
            FROM documento d, carpeta c, subcarpeta s 
            WHERE d.carpeta = c.idcarpeta AND d.subcarpeta = s.idsubcarpeta AND c.idcarpeta = s.carpeta_id AND d.estado_documento = 1 AND c.idcarpeta = '{0}'
            ORDER BY d.fecha_documento ASC""".format(carpeta)
    cursor.execute(sql)
    docs = cursor.fetchall()
    if docs:
        registro = docs[0]
    else:
        registro = ''
    data = { 'titulo': 'Formatos Encontrados',
            'encabezado': registro
            }
    return render_template('listado.html',data=data, docs=docs)

@listados.route('/listado/sort/search/<carpeta>', methods=['POST'])
@login_required
def lista_sort_search(carpeta):
    if request.method == 'POST':
        b = request.form['search_input']
        busqueda = b.replace("'","")

    cursor = conexion.connection.cursor()
    sql = """SELECT d.iddocumento, c.nombre_carpeta, s.nombre_subcarpeta, d.nombre_documento, d.fecha_documento, d.version_documento, c.idcarpeta, s.idsubcarpeta, d.estado_documento 
            FROM documento d, carpeta c, subcarpeta s 
            WHERE d.carpeta = c.idcarpeta AND d.subcarpeta = s.idsubcarpeta AND c.idcarpeta = s.carpeta_id AND d.estado_documento = 1 AND c.idcarpeta = '{0}' 
            AND CONCAT(d.nombre_documento,' ',c.nombre_carpeta,' ',s.nombre_subcarpeta,' ',date_format(d.fecha_documento, "%d/%m/%Y")) LIKE '%{1}%' 
            ORDER BY d.nombre_documento ASC""".format(carpeta,busqueda)
    cursor.execute(sql)
    docs = cursor.fetchall()
    if docs:
        registro = docs[0]
    else:
        registro = ''
    data = { 'titulo': 'Formatos Encontrados',
            'encabezado': registro
            }
    return render_template('listado.html',data=data, docs=docs)


@listados.route('/listado/sortsub/file/<subcarpeta>')
@login_required
def lista_sortsub(subcarpeta):
    cursor = conexion.connection.cursor()
    sql = """SELECT d.iddocumento, c.nombre_carpeta, s.nombre_subcarpeta, d.nombre_documento, d.fecha_documento, d.version_documento, c.idcarpeta, s.idsubcarpeta, d.estado_documento 
            FROM documento d, carpeta c, subcarpeta s 
            WHERE d.carpeta = c.idcarpeta AND d.subcarpeta = s.idsubcarpeta AND c.idcarpeta = s.carpeta_id AND d.estado_documento = 1 AND s.idsubcarpeta = '{0}' 
            ORDER BY d.nombre_documento ASC""".format(subcarpeta)
    cursor.execute(sql)
    docs = cursor.fetchall()
    if docs:
        registro = docs[0]
    else:
        registro = ''
    data = { 'titulo': 'Formatos Encontrados',
            'encabezado': registro,
            'sub': True
            }
    return render_template('listado.html',data=data, docs=docs)

@listados.route('/listado/sortsub/date/<subcarpeta>')
@login_required
def lista_sortsub_date(subcarpeta):
    cursor = conexion.connection.cursor()
    sql = """SELECT d.iddocumento, c.nombre_carpeta, s.nombre_subcarpeta, d.nombre_documento, d.fecha_documento, d.version_documento, c.idcarpeta, s.idsubcarpeta, d.estado_documento 
            FROM documento d, carpeta c, subcarpeta s 
            WHERE d.carpeta = c.idcarpeta AND d.subcarpeta = s.idsubcarpeta AND c.idcarpeta = s.carpeta_id AND d.estado_documento = 1 AND s.idsubcarpeta = '{0}' 
            ORDER BY d.fecha_documento ASC""".format(subcarpeta)
    cursor.execute(sql)
    docs = cursor.fetchall()
    if docs:
        registro = docs[0]
    else:
        registro = ''
    data = { 'titulo': 'Formatos Encontrados',
            'encabezado': registro,
            'sub': True
            }
    return render_template('listado.html',data=data, docs=docs)

@listados.route('/listado/sortsub/search/<subcarpeta>', methods=['POST'])
@login_required
def lista_sortsub_search(subcarpeta):
    if request.method == 'POST':
        b = request.form['search_input']
        busqueda = b.replace("'","")

    cursor = conexion.connection.cursor()
    sql = """SELECT d.iddocumento, c.nombre_carpeta, s.nombre_subcarpeta, d.nombre_documento, d.fecha_documento, d.version_documento, c.idcarpeta, s.idsubcarpeta, d.estado_documento 
            FROM documento d, carpeta c, subcarpeta s 
            WHERE d.carpeta = c.idcarpeta AND d.subcarpeta = s.idsubcarpeta AND c.idcarpeta = s.carpeta_id AND d.estado_documento = 1 AND s.idsubcarpeta = '{0}'
            AND CONCAT(d.nombre_documento,' ',c.nombre_carpeta,' ',s.nombre_subcarpeta,' ',date_format(d.fecha_documento, "%d/%m/%Y")) LIKE '%{1}%' 
            ORDER BY d.nombre_documento ASC""".format(subcarpeta, busqueda)
    cursor.execute(sql)
    docs = cursor.fetchall()
    if docs:
        registro = docs[0]
    else:
        registro = ''
    data = { 'titulo': 'Formatos Encontrados',
            'encabezado': registro,
            'sub': True
            }
    return render_template('listado.html',data=data, docs=docs)

@listados.route('/listado/search/', methods=['POST'])
@login_required
def lista_search():
    if request.method == 'POST':
        b = request.form['search_input']
        busqueda = b.replace("'","")

    cursor = conexion.connection.cursor()
    sql = """SELECT d.iddocumento, c.nombre_carpeta, s.nombre_subcarpeta, d.nombre_documento, d.fecha_documento, d.version_documento, c.idcarpeta, s.idsubcarpeta, d.estado_documento 
            FROM documento d, carpeta c, subcarpeta s 
            WHERE d.carpeta = c.idcarpeta AND d.subcarpeta = s.idsubcarpeta AND d.estado_documento = 1 AND c.idcarpeta = s.carpeta_id 
            AND CONCAT(d.nombre_documento,' ',c.nombre_carpeta,' ',s.nombre_subcarpeta,' ',date_format(d.fecha_documento, "%d/%m/%Y")) LIKE '%{0}%' 
            ORDER BY d.nombre_documento ASC""".format(busqueda)
    cursor.execute(sql)
    docs = cursor.fetchall()
  
    data = { 'titulo': 'Resultados de la Busqueda',
            'encabezado': False,
            'busqueda': busqueda
            }
    return render_template('listado.html',data=data, docs=docs)
    
# ----------------- Fin Rutas Listado -----------------------
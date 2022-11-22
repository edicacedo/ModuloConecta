from .entities.User import User

class ModelUser():

    @classmethod
    def login(self, conexion, user):
        try:
            cursor = conexion.connection.cursor()
            sql = """SELECT idusuario, username, password, nombre_usuario, correo_usuario, telefono_usuario, estado_usuario, rol_usuario
                     FROM usuario 
                     WHERE username = '{0}' """.format(user.username)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                usuario = User(row[0],row[1],User.check_password(row[2],user.password),row[3],row[4],row[5],row[6],row[7])
                return usuario
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    def obtener_usuario(conexion, id):
        try:
            cursor = conexion.connection.cursor()
            sql = """SELECT idusuario, username, password, nombre_usuario, correo_usuario, telefono_usuario, estado_usuario, rol_usuario
                     FROM usuario 
                     WHERE idusuario = '{}' """.format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return User(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

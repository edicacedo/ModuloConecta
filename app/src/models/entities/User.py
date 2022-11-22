from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class User(UserMixin):

    def __init__(self, idusuario, username, password, nombre_usuario="", correo_usuario="", telefono_usuario="", estado_usuario="", rol_usuario="") -> None:
        self.id = idusuario
        self.username = username
        self.password = password
        self.nombre_usuario = nombre_usuario
        self.correo_usuario = correo_usuario
        self.telefono_usuario = telefono_usuario
        self.estado_usuario = estado_usuario
        self.rol_usuario = rol_usuario

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password,password)

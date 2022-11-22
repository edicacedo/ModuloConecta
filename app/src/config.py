from flask import Flask, jsonify, render_template, request, url_for, redirect, flash
from flask_mysqldb import MySQL
#para archivos
import os
import errno
from os import remove, rmdir
from pathlib import Path
from os.path import join, dirname, realpath
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
#Login
from flask_login import login_manager, login_user, logout_user, login_required, current_user
from flask_wtf.csrf import CSRFProtect

#Models:
from models.ModelUser import ModelUser

#Entities:
from models.entities.User import User

class Config:
    SECRET_KEY = 'hJ%q6oe4m@jeC&V@Y!VA!tOL_'

class DevelopmentConfig(Config):
    DEBUG=True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'conec7a_docs'
    MYSQL_PORT = 3308
    UPLOAD_FOLDER = './static/archivos/'

config = {
    'development': DevelopmentConfig
}
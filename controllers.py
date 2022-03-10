
from flask.views import MethodView
from flask import jsonify, request, session
from model import users
import hashlib
import bcrypt # pip3 install bcrypt
import jwt # pip3 install pyjwt
from config import KEY_TOKEN_AUTH
import datetime
import pymysql
from validators import CreateRegisterSchema

def crear_conexion():
    try:
        #conexion a la db
        conexion = pymysql.connect(host='localhost',user='root',passwd='',db="tiendaarqsoft" )
        return conexion
    except pymysql.Error as error:
        print('Se ha producido un error al crear la conexión:', error)


class RegisterControllers(MethodView):
    """
        Example register
    """
    def post(self):
        content = request.get_json()
        create_register_schema = CreateRegisterSchema()
                
        errors = create_register_schema.validate(content)
        if errors:
            return errors, 400
        correo = content.get("email")
        password = content.get("password")
        nombres = content.get("nombre")
        salt = bcrypt.gensalt()
        hash_password = bcrypt.hashpw(bytes(str(password), encoding= 'utf-8'), salt)
        print(hash_password)
        conexion=crear_conexion()
        print(conexion)
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT clave,correo FROM registro_usuario WHERE correo=%s", (correo, ))
        auto=cursor.fetchone()
        if auto==None:
            cursor.execute(
                 "INSERT INTO registro_usuario(correo,nombre,clave) VALUES(%s,%s,%s)", (correo,nombres,hash_password,))
            conexion.commit()
            conexion.close()
            return ("bienvenido registro exitoso")
        else :    
            conexion.commit()
            conexion.close()
            print( "el usuario ya esta registrado")
            return ("el usuario ya esta registrado")



class LoginControllers(MethodView):
    """
        Example Login
    """
    def post(self):
        content = request.get_json()
        clave = content.get("password")
        correo = content.get("email")
        print("--------", users, content.get("clave"), correo)
        conexion=crear_conexion()
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT clave,correo,nombre FROM registro_usuario WHERE correo=%s", (correo, )
        )
        auto = cursor.fetchone()
        conexion.close()
        print(auto)
        if auto==None:
            return jsonify({"Status": "usuario no registrado 22"}), 400
        
        if (auto[1]==correo):
            if  bcrypt.checkpw(clave.encode('utf8'), auto[0].encode('utf8')):
                encoded_jwt = jwt.encode({'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=300), 'email': correo,'Rol':"User"}, KEY_TOKEN_AUTH , algorithm='HS256')
                return jsonify({"Status": "loguin exitoso","usuario: "+auto[2]+"token": encoded_jwt}), 200
        else:
            return jsonify({"Status": "correo o clave incorrecta"}), 400
#############################################



class JsonControllers(MethodView):
    """
        Example Json
    """
    def post(self):
        content = request.get_json()
        nombres = content.get("nombres")
        return jsonify({"Status": "JSON recibido y procesado correctamente","nombre": nombres}), 200


class StockControllers(MethodView):
    """
        Example verify Token
    """
    def get(self):
        if (request.headers.get('Authorization')):
            token = request.headers.get('Authorization').split(" ")
            print("-----------------_", token[1])
            try:
                data = jwt.decode(token[1], KEY_TOKEN_AUTH , algorithms=['HS256'])
                conexion=crear_conexion()
                cursor = conexion.cursor()
                cursor.execute("SELECT clave,correo,nombre FROM registro_usuario WHERE correo=%s", (token[1], ))
                auto = cursor.fetchone()
                conexion.close()
                print("si estafuncionando")
                return jsonify({"Status": "Autorizado por token", "emailextraido": data.get("email"), "stock": auto}), 200
                return jsonify({"Status": "Autorizado por token", "emailextraido": data.get("email"),}), 200
            except:
                return jsonify({"Status": "TOKEN NO VALIDO"}), 403
        return jsonify({"Status": "No ha enviado un token"}), 403

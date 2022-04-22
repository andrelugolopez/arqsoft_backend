
from flask.views import MethodView
from flask import jsonify, request, session
#from model import users
import hashlib
import pymysql
import bcrypt
import jwt
from config import KEY_TOKEN_AUTH
import datetime
from validators import CreateRegisterSchema
from validators import CreateLoginSchema
from validators import CreateProductoSchema

def crear_conexion():
    try:
        conexion = pymysql.connect(host='localhost',user='root',passwd='',db="talle_e" )
        return conexion
    except pymysql.Error as error:
        print('Se ha producido un error al crear la conexión:', error)


create_register_schema = CreateRegisterSchema()
create_login_schema = CreateLoginSchema()
create_producto_schema = CreateProductoSchema()
class RegisterControllers(MethodView):
    def post(self):
        content = request.get_json()
        email = content.get("email")
        nombres = content.get("nombres")
        apellidos = content.get("apellidos")
        password = content.get("password")
        documento= content.get("cedula")
        ##print("--------",email, nombres,apellidos,password,documento)
        salt = bcrypt.gensalt()
        hash_password = bcrypt.hashpw(bytes(str(password), encoding= 'utf-8'), salt)
        errors = create_register_schema.validate(content)
        if errors:
            return errors, 400
        conexion=crear_conexion()
        print(conexion)
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT Password,Correo FROM usuarios WHERE correo=%s", (email, ))
        auto=cursor.fetchone()
        if auto==None:
            cursor.execute(
                 "INSERT INTO usuarios (Correo,Nombres,Apellidos,Password,Documento) VALUES(%s,%s,%s,%s,%s)", (email,nombres,apellidos,hash_password,documento,))
            conexion.commit()
            conexion.close()
            return jsonify({"Status": "Bienvenido registro exitoso"}), 200
        else :    
            conexion.commit()
            conexion.close()
            return jsonify({"Status": "El usuario ya esta registrado"}), 200

class LoginControllers(MethodView):
    def post(self):
        content = request.get_json()
        #Instanciar la clase
        create_login_schema = CreateLoginSchema()
        errors = create_login_schema.validate(content)
        if errors:
            return errors, 400
        clave = content.get("password")
        correo = content.get("email")
        print(content.get("password"), correo)
        conexion=crear_conexion()
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT Password,Correo,Nombres,Apellidos FROM usuarios WHERE correo=%s", (correo,)
        )
        auto = cursor.fetchone()
        conexion.close()
        print(auto)
        if auto==None:
            return jsonify({"Status": "usuario no registrado 22"}), 400
        
        if (auto[1]==correo):
            if  bcrypt.checkpw(clave.encode('utf8'), auto[0].encode('utf8')):
                encoded_jwt = jwt.encode({'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=300), 'email': correo}, KEY_TOKEN_AUTH , algorithm='HS256')
                return jsonify({"Status": "login exitoso","into": encoded_jwt}), 200
        else:
            return jsonify({"Status": "Correo o Clave incorrecta"}), 400

## para modulo admin, creacion de productos
# class CrearControllers(MethodView):
#     def post(self):
#         content = request.get_json()
#         precio = content.get("precio")
#         nombre = content.get("nombre")
#         if (request.headers.get('Authorization')):
#                 token = request.headers.get("Authorization").split(" ")
#                 try:
#                     decoded_jwt = jwt.decode(token[1], KEY_TOKEN_AUTH , algorithms=['HS256'])
#                     errors = create_producto_schema.validate(content)
#                     if errors:
#                         return errors, 400
#                     conexion=crear_conexion()
#                     cursor = conexion.cursor()
#                     cursor.execute("INSERT INTO productos (Nombre,Precio) VALUES(%s,%s)", (nombre,precio,))
#                     conexion.commit()
#                     conexion.close()
#                     return jsonify({"Status": "Autorizado por token", "Nuevo producto": "ok"}), 200
#                 except:
#                     return jsonify({"Status": "Token invalido"}), 400
#         return jsonify({"Status": "No ha enviado un token"}), 403
        

## para el modulo de tienda cargar los productos de la base de datos

# class ProductosControllers(MethodView):
#     def get(self):
#         #consulta base de datos
#         conexion=crear_conexion()
#         cursor = conexion.cursor()
#         cursor.execute("SELECT * FROM productos")
#         conexion.commit()
#         conexion.close()
#         auto=cursor.fetchall()
#         print("productos facturados",auto)
#         return jsonify(auto), 200

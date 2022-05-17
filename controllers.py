# nombres usados para seguridad
# envio de token = into
# nombre de usuario = Nuat
# rol =n3yB6PZnGE8n7F
# admin=J8p4SBfJgRfZCo
# tecnico=H7qm7gQr6DBGfM
# usuario=hbh2jFVsQM7RUy


from flask.views import MethodView
from flask import jsonify, request, session
#from model import users
import hashlib
import pymysql.cursors
import bcrypt
import jwt
from config import KEY_TOKEN_AUTH
import datetime

from validators import CreateRegisterSchema
from validators import CreateLoginSchema

# def crear_conexion():
#     try:
#         conexion = pymysql.connect(host='201.190.114.194',user='root',password='secret',port= 39009,db="database_user",charset='utf8mb4' )

#         return conexion
#     except pymysql.Error as error:
#         print('Se ha producido un error al crear la conexión:', error)


def crear_conexion():
    try:
        conexion = pymysql.connect(host='localhost',user='root',passwd='Sena1234',db="database_user",charset='utf8mb4' )
        return conexion
    except pymysql.Error as error:
        print('Se ha producido un error al crear la conexión:', error)

def crear_conexionMongo():
    try:
        conexion = pymysql.connect(host='localhost',user='root',passwd='Sena1234',db="pruebatienda",charset='utf8mb4')
        return conexion
    except pymysql.Error as error:
        print('Se ha producido un error al crear la conexión:', error)


create_register_schema = CreateRegisterSchema()
create_login_schema = CreateLoginSchema()


class RegisterControllers(MethodView):
    def post(self):
        print ("registro de usuarios admin y tecnicos")
        rol="hbh2jFVsQM7RUy"
        content = request.get_json()
        email = content.get("email")
        nombres = content.get("nombres")
        apellidos = content.get("apellidos")
        password = content.get("password")
        documento= content.get("cedula")
        print("--------",email, nombres,apellidos,password,documento)
        salt = bcrypt.gensalt()
        hash_password = bcrypt.hashpw(bytes(str(password), encoding= 'utf-8'), salt)
        errors = create_register_schema.validate(content)
        if errors:
            return errors, 400
        conexion=crear_conexion()
        print(conexion)
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT clave,correo FROM usuarios WHERE correo=%s", (email, ))
        auto=cursor.fetchone()
        if auto==None:
            cursor.execute(
                "INSERT INTO usuarios (correo,nombres,apellidos,clave,documento,rol) VALUES(%s,%s,%s,%s,%s,%s)", (email.lower(),nombres.capitalize(),apellidos.capitalize(),hash_password,documento,rol,))
            conexion.close()
            return jsonify({"Status": "Bienvenido registro exitoso"}), 200
        else :    
            conexion.commit()
            conexion.close()
            return jsonify({"Status": "El usuario ya esta registrado"}), 200
class LoginControllers(MethodView):
    def post(self):
        print ("login y creacion de jwt para navegacion")
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
        # cursor.execute(
        #     "SELECT clave,correo,nombres,apellidos,rol,documento FROM usuarios WHERE correo=%s", (correo,)
        # )
        cursor.execute(
            "SELECT Password,Email,Nombres,Apellidos,Rol,Documento FROM usuarios WHERE Email=%s", (correo,)
        )
        auto = cursor.fetchone()
        conexion.close()
        print( "datos", auto)
        if auto==None:
            return jsonify({"Status": "usuario no registrado 22"}), 403
        
        if (auto[1]==correo):
            if  bcrypt.checkpw(clave.encode('utf8'), auto[0].encode('utf8')):
                encoded_jwt = jwt.encode(
                    {'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=3600),
                    'email': correo,
                    'user':auto[2] ,
                    'rol':auto[4]}, 
                    KEY_TOKEN_AUTH , algorithm='HS256')
                return jsonify({"Status": "login exitoso","into": encoded_jwt,'Nuat':auto[2],'n3yB6PZnGE8n7F':auto[4],'doc': auto[5]}), 200
            else:
                return jsonify({"Status": "Clave incorrecta"}), 400

## para el modulo de tienda cargar los productos de la base de datos
#http://127.0.0.1:5000/productos/tipo=?R o P o E
class ProductosControllers(MethodView):
    def get(self):
        print ("consulta todos los productos de la tienda")
        Tproducto= request.args.get("tipo") # asi es que envia por cabecera la categoría seleccionada - headers idproducto - R001
        #consulta base de datos
        conexion=crear_conexionMongo()
        cursor = conexion.cursor(pymysql.cursors.DictCursor)
        #Se formatea la consulta y se envia parametro de consulta en un arreglo
        cursor.execute(
            f"select * from productos where idproducto like '{Tproducto}%'");
        productos=cursor.fetchall()
        conexion.commit()
        conexion.close()
        print("Lista de productos",productos)
        return jsonify({'data':productos}), 200

## consulta a la base de datos el producto y se le agrega al usuario

#http://127.0.0.1:5000/productoId/id_producto=?R120 o P349 o E998
class ProductoIdControllers(MethodView):
    def post(self):
        id_producto =request.args.get("idproducto") ## se espera llegada de id del producto
        print("***** Id a consultar", id_producto)
        conexion=crear_conexionMongo()
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT idproducto,nombre,cantidad,precio,imagen FROM productos WHERE idproducto=%s", (id_producto,))
        dato=cursor.fetchone()
        print("dato del producto",dato)
        conexion.commit()
        conexion.close()
        if dato==None:
            return jsonify({"Status": "articulo no esta creado 33"}), 403
        return jsonify({'status':'envio ok','data':dato}), 200

## para modulo admin, creacion de productos
class CrearControllers(MethodView):
    def post(self):
        print ("crear producto en la tienda")
        content = request.get_json()
        id_producto=content.get("idproducto")
        precio = content.get("precio")
        nombre = content.get("nombre")
        cantidad= content.get("cantidad")
        imagen=content.get("imagen")
        if (request.headers.get('Authorization')):
            token = request.headers.get('Authorization').split(" ")
            try:
                data = jwt.decode(token[1], KEY_TOKEN_AUTH , algorithms=['HS256'])
                if (data.get('rol')=='admin'):
                    conexion=crear_conexionMongo()
                    cursor = conexion.cursor()
                    cursor.execute("INSERT INTO productos (idproducto,nombre,cantidad,precio,imagen) VALUES(%s,%s,%s,%s,%s)", (id_producto,nombre,cantidad,precio,imagen,))
                    conexion.commit()
                    conexion.close()
                    print("--Artuculo guardado en la BD--")
                else:
                    return jsonify({"Status": "No autorizado por token"}), 403
                return jsonify({"Status": "Autorizado por token", "emailextraido": data.get("email"),}), 200
            except:
                return jsonify({"Status": "TOKEN NO VALIDO"}), 403
        return jsonify({"Status": "No ha enviado un token"}), 403

## para modulo admin, eliminar de productos
class EliminarProductoControllers(MethodView):
    def get(self):
        idproducto= request.args.get("idproe")
        print ("eliminar producto de la tienda")
        if (request.headers.get('Authorization')):
            token = request.headers.get('Authorization').split(" ")
            try:
                data = jwt.decode(token[1], KEY_TOKEN_AUTH , algorithms=['HS256'])
                if (data.get('rol')=='admin'):
                    conexion=crear_conexionMongo()
                    cursor = conexion.cursor()
                    cursor.execute("DELETE FROM productos WHERE idproducto=%s",(idproducto,))
                    conexion.commit()
                    conexion.close()
                    print("--Artuculo eliminado de la BD--")
                else:
                    return jsonify({"Status": "No autorizado por token"}), 403
                return jsonify({"Status": "Autorizado por token", "emailextraido": data.get("email"),}), 200
            except:
                return jsonify({"Status": "TOKEN NO VALIDO"}), 403
        return jsonify({"Status": "No ha enviado un token"}), 403

## para modulo admin, eliminar de productos

class EliminarUserControllers(MethodView):
    def get(self):
        correo= request.args.get("correo")
        print ("eliminar usuario del sistema")
        if (request.headers.get('Authorization')):
            token = request.headers.get('Authorization').split(" ")
            try:
                data = jwt.decode(token[1], KEY_TOKEN_AUTH , algorithms=['HS256'])
                if (data.get('rol')=='admin'):
                    conexion=crear_conexion()
                    cursor = conexion.cursor()
                    cursor.execute("DELETE FROM usuarios WHERE Email=%s",(correo,))
                    conexion.commit()
                    conexion.close()
                    print("--Artuculo eliminado de la BD--")
                else:
                    return jsonify({"Status": "No autorizado por token"}), 403
                return jsonify({"Status": "Autorizado por token", "emailextraido": data.get("email"),}), 200
            except:
                return jsonify({"Status": "TOKEN NO VALIDO"}), 403

        return jsonify({"Status": "No ha enviado un token"}), 403
#UPDATE `usuarios` SET `Nombres` = 'Manuela', `Apellidos` = 'Madrid Caro' WHERE `usuarios`.`Email` = 'manuelacaro@gmail.com';
## para modulo admin, eliminar de usuarios
# class ActualizarUserControllers(MethodView):
#     def post(self):
#         content = request.get_json()
#         email = content.get("email")
#         conexion=crear_conexion()
#         cursor = conexion.cursor()
#         cursor.execute("SELECT Email,Nombres,Apellidos,Rol FROM usuarios WHERE Email=%s", (correo,))
#         conexion.commit()
#         conexion.close()
#         print("-- datos leidos de la BD --")
#         nombres = content.get("nombres")
#         apellidos = content.get("apellidos")
#         documento= content.get("cedula")
#         rol= content.get("rol")
#         telefono = content.get("rol")
#         errors = create_register_schema.validate(content)
#         if errors:
#             return errors, 400
#         conexion=crear_conexion()
#         print(conexion)
#         cursor = conexion.cursor()
#         cursor.execute(
#             "SELECT Password,Email FROM usuarios WHERE Email=%s", (email, ))
#         auto=cursor.fetchone()
#         print ("actualiar usuario en el sistema")
#         if (request.headers.get('Authorization')):
#             token = request.headers.get('Authorization').split(" ")
#             try:
#                 data = jwt.decode(token[1], KEY_TOKEN_AUTH , algorithms=['HS256'])
#                 if (data.get('rol')=='admin'):
#                     conexion=crear_conexion()
#                     cursor = conexion.cursor()
#                     # cursor.execute("DELETE FROM usuarios WHERE Email=%s",(correo,))
#                     cursor.execute(UPDATE `usuarios` SET `Nombres` = 'Manuela', `Apellidos` = 'Madrid Caro' WHERE `usuarios`.`Email` = 'manuelacaro@gmail.com')
#                     conexion.commit()
#                     conexion.close()
#                     print("--Artuculo eliminado de la BD--")
#                 else:
#                     return jsonify({"Status": "No autorizado por token"}), 403
#                 return jsonify({"Status": "Autorizado por token", "emailextraido": data.get("email"),}), 200
#             except:
#                 return jsonify({"Status": "TOKEN NO VALIDO"}), 403
#         return jsonify({"Status": "No ha enviado un token"}), 403

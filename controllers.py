# nombres usados para seguridad
# envio de token = into
# nombre de usuario = Nuat
# rol =n3yB6PZnGE8n7F
# admin=J8p4SBfJgRfZCo
# tecnico=H7qm7gQr6DBGfM
# usuario=hbh2jFVsQM7RUy


from flask.views import MethodView
from flask import jsonify, request, session
import hashlib
import pymongo
import pymysql.cursors
import bcrypt
import jwt
from config import KEY_TOKEN_AUTH
import datetime
import random
import korreo
from validators import CreateRegisterSchema
from validators import CreateLoginSchema

def gen_codigo(tamaño):
    chars = list('ABCDEFGHIJKLMNOPQRSTUVWYZabcdefghijklmnopqrstuvwyz01234567890')
    random.shuffle(chars)
    chars = ''.join(chars)
    sha1 = hashlib.sha1(chars.encode('utf8'))
    codigo = sha1.hexdigest()[:tamaño]
    return codigo

def crear_conexion():
    try:
        conexion = pymysql.connect(host='jhtserverconnection.ddns.net',user='root',password='secret',port= 39009,db="database_user",charset='utf8mb4' )
        return conexion
    except pymysql.Error as error:
        print('Se ha producido un error al crear la conexión:', error)
        

def crear_conexionMongo():
    MONGO_HOST="jhtserverconnection.ddns.net"
    MONGO_PUERTO="39011"
    MONGO_TIEMPO_FUERA=1000
    MONGO_URI="mongodb://"+MONGO_HOST+":"+MONGO_PUERTO+"/"
    try:
        cliente=pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
        cliente.server_info()
        print("Conexion a mongo exitosa")
        ###cliente.close()
        ##return conexion
    except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
        print("Tiempo excedido  ",errorTiempo)
    except pymongo.errors.ConnectionFailure as errorConexion:
        print("Fallo al conectarse a mongodb ",errorConexion)

create_register_schema = CreateRegisterSchema()
create_login_schema = CreateLoginSchema()


class RegisterControllers(MethodView):
    def post(self):
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
            conexion.commit()
            conexion.close()
            return jsonify({"Status": "Bienvenido registro exitoso"}), 201
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
        cursor.execute(
            "SELECT clave,correo,nombres,apellidos,rol,documento FROM usuarios WHERE correo=%s", (correo,)
        )
        auto = cursor.fetchone()
        conexion.close()
        print( "datos", auto)
        if auto==None:
            return jsonify({"Status": "usuario no registrado"}), 400
        
        if (auto[1]==correo):
            if  bcrypt.checkpw(clave.encode('utf8'), auto[0].encode('utf8')):
                encoded_jwt = jwt.encode(
                    {'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=3600),
                    'email': correo,
                    'user':auto[2] ,
                    'rol':auto[4]}, 
                    KEY_TOKEN_AUTH , algorithm='HS256')

                return jsonify({"Status": "login exitoso","into": encoded_jwt,'Nuat':auto[2],'n3yB6PZnGE8n7F':auto[4],'doc':auto[5]}), 200
            else:
                return jsonify({"Status": "Clave incorrecta"}), 403

## para el modulo de tienda cargar los productos de la base de datos
#http://127.0.0.1:5000/productos/tipo=?R o P o E
class ProductosControllers(MethodView):
    def get(self):
        print ("consulta todos los productos de la tienda")
        Tproducto= request.args.get("tipo") # asi es que envia por cabecera la categoría seleccionada - headers idproducto - R001
        #consulta base de datos
        MONGO_HOST="jhtserverconnection.ddns.net"
        MONGO_PUERTO="39011"
        MONGO_TIEMPO_FUERA=1000
        MONGO_URI="mongodb://"+MONGO_HOST+":"+MONGO_PUERTO+"/"
        cliente=pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)

        mydb = cliente[ "dbproductos"]
        mycol = mydb[ "productos"]

        myquery = { "idproducto": { "$regex": Tproducto } }
        productos = mycol.find(myquery)

        keys = ["_id"]
        output = []
        for producto in productos:
            output.append({x:producto[x] for x in producto if x not in keys})
        print(output)
        print("Lista de productos",productos)
        return jsonify({'data':output}), 200

## consulta a la base de datos el producto y se le agrega al usuario

#http://127.0.0.1:5000/productoId/id_producto=?R120 o P349 o E998
class ProductoIdControllers(MethodView):
    def get(self):
        print ("consulta todos los productos de la tienda")
        id_producto=request.args.get("idproducto") # asi es que envia por cabecera la categoría seleccionada - headers idproducto - R001
        MONGO_HOST="jhtserverconnection.ddns.net"
        MONGO_PUERTO="39011"
        MONGO_TIEMPO_FUERA=1000
        MONGO_URI="mongodb://"+MONGO_HOST+":"+MONGO_PUERTO+"/"
        producto=pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)

        mydb = producto["dbproductos"]
        mycol = mydb["productos"]

        myquery = { "idproducto": { "$regex": id_producto } }
        info = mycol.find(myquery)
        keys = ["_id"]
        producto=producto not in keys
        print("dato del producto",producto)
        return jsonify({'status':'envio ok','data':producto}), 200

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
                if (data.get('rol')=='J8p4SBfJgRfZCo'):
                    conexion=crear_conexionMongo()
                    cursor = conexion.cursor()
                    cursor.execute("INSERT INTO productos (idproducto,nombre,cantidad,precio,imagen) VALUES(%s,%s,%s,%s,%s)", (id_producto,nombre,cantidad,precio,imagen,))
                    conexion.commit()
                    conexion.close()
                    print("--Artuculo guardado en la BD--")
                else:
                    return jsonify({"Status": "No autorizado por token"}), 498
                return jsonify({"Status": "Autorizado por token", "emailextraido": data.get("email"),}), 202
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
                    return jsonify({"Status": "No autorizado por token"}), 498
                return jsonify({"Status": "Autorizado por token", "emailextraido": data.get("email"),}), 200
            except:
                return jsonify({"Status": "TOKEN NO VALIDO"}), 498
        return jsonify({"Status": "No ha enviado un token"}), 203

class CambioClaveControllers(MethodView):
    def post(self):
        content = request.get_json()
        email =content.get("email") 
        newPassword =content.get("password")
        salt = bcrypt.gensalt()
        hash_password = bcrypt.hashpw(bytes(str(newPassword), encoding= 'utf-8'), salt)
        errors = create_login_schema.validate(content)
        if errors:
            return errors, 400
        conexion=crear_conexion()
        cursor = conexion.cursor()
        sql = "UPDATE usuarios SET clave = %s WHERE correo = %s"
        val = (hash_password,email)
        cursor.execute(sql,val)
        conexion.commit()
        conexion.close()
        return jsonify({'status':'clave actualizada satisfactoriamente'}), 200

########## aporte faber

class OrdenServicioControllers(MethodView):
    def post(self):
        content = request.get_json()
        nombre = content.get("nombre")
        telefono = content.get("telefono")
        cedula = content.get("cedula")
        #codservicio = content.get("codservicio")
        codtecnico = content.get("codtecnico")
        marcadispositivo = content.get("marcadispositivo")
        tipodispositivo = content.get("tipodispositivo")
        tiposervicio = content.get("tiposervicio")
        accesorios = content.get("accesorios")
        diaginicial = content.get("diaginicial")
        codservicio = gen_codigo(5)
        #consulta base de datos
        conexion=crear_conexion()
        cursor = conexion.cursor()
        #Se formatea la consulta y se envia parametro de consulta en un arreglo
        cursor.execute(
            #f"select * from productos where idproducto like '{idproduc}%'");
            "INSERT INTO ordenservicio (nombre,telefono,cedula,codservicio,codtecnico,marcadispositivo,tipodispositivo,tiposervicio,accesorios,diaginicial) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (nombre,telefono,cedula,codservicio,codtecnico,marcadispositivo,tipodispositivo,tiposervicio,accesorios,diaginicial,)
            )
        conexion.commit()
        auto=cursor.fetchall()
        #print("Mostra orden de servicio",auto)
        conexion.close()
        return jsonify({"Status": "Orden de servicio almacenada correctamente"}), 200

class ConsultaOrdenControllers(MethodView):
    def post(self):
        rol="hbh2jFVsQM7RUy"
        content = request.get_json()
        correo = content.get("email")
        nombres = content.get("nombre")
        apellidos=content.get("apellidos")
        telefono= content.get("telefono")
        documento= content.get("cedula")
        password = content.get("cedula")
        print ("llega de front",content)
        salt = bcrypt.gensalt()
        hash_password = bcrypt.hashpw(bytes(str(password), encoding= 'utf-8'), salt)
        # conexion=crear_conexion()
        # cursor = conexion.cursor()
        # print(conexion)
        if(correo!=""):
            sql = "SELECT correo,nombres,apellidos,documento FROM usuarios WHERE correo=%s"
            adr= correo
            cursor.execute(sql,adr) 
            datos=cursor.fetchone()
        elif(documento!=""):
            sql = "SELECT correo,nombres,apellidos,documento FROM usuarios WHERE documento=%s"
            adr= documento
            cursor.execute(sql,adr) 
            datos=cursor.fetchone()
        elif(telefono!=""):
            sql = "SELECT correo,nombres,apellidos,documento FROM usuarios WHERE telefono=%s"
            adr= telefono
            cursor.execute(sql,adr) 
            datos=cursor.fetchone()
        else:
            cursor.execute("INSERT INTO usuarios (correo,nombres,apellidos,clave,documento,rol) VALUES(%s,%s,%s,%s,%s,%s)", (correo.lower(),nombres.capitalize(),apellidos.capitalize(),hash_password,documento,rol,))
            conexion.commit()
            conexion.close()
            print("usuario registrado")
        print ("sale del back",datos)
        if datos==None:
            return jsonify({"Status": "El usuario no se encuentra registrado"}), 201
        else :
            return jsonify({"Status": "El usuario si esta registrado", "data":datos}), 200 

        return jsonify({"Status": "Consulta Orden "}), 200

## para el modulo de tienda - asignación de técnico ***************************************************
#http://127.0.0.1:5000/asignaciontecnico

class AsignacionTecnicoControllers(MethodView):
    def post(self):
        content = request.get_json()
        #Campos del formulario
        tipodispositivo = content.get("tipodispositivo")
        codtecnico = request.args.get("id_tec")
        nombretecnico = content.get("nombretecnico")
        codservicio = request.args.get("codservicio")
        escalarservicio = content.get("escalarservicio")
        tipoespeciescalar = content.get("tipoespeciescalar")
        diaginicial = content.get("diaginicial")
        #consulta base de datos database_user
        conexion=crear_conexion()
        cursor = conexion.cursor()
        #Se formatea la consulta y se envia parametro de consulta en un arreglo
        cursor.execute(
            f" SELECT * FROM usuarios WHERE id_tec like '{codtecnico}%'"
            )
        listatecnicos=cursor.fetchall()
        print("Lista de técnicos",listatecnicos)
        conexion.close()
        return jsonify({"Status":"Lista de técnicos",'data':listatecnicos}), 200
        conexion=crear_conexion_productos()
        cursor = conexion.cursor()
        #Se formatea la consulta y se envia parametro de consulta en un arreglo
        cursor.execute(
            f" SELECT * FROM asignaciontecnico WHERE codservicio =%s", (codservicio,)
            )
        mostradiagnostico=cursor.fetchone()
        print("Diagnóstico",mostradiagnostico)
        conexion.close()
        return jsonify({"Status":"Diagnóstico",'data':mostradiagnostico}), 200


class TokenContrasenaControllers(MethodView):
    def post(self):
        usuario="Querido usuario"
        content = request.get_json()
        email =content.get("email")
        print("--------",email)
        cod=gen_codigo(8)
        korreo.send_correo(usuario,email,cod)
        print("CodigoR",cod)
        print('Longitud del Token de recuperación',len(cod))
        return jsonify({'Status':'Token generado','CodigoR':cod}), 200
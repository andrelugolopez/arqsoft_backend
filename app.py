from flask import Flask
from routes import *
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

app.add_url_rule(routes["register"], view_func=routes["register_controllers"])
app.add_url_rule(routes["registerAdmin"], view_func=routes["registerAdmin_controllers"])
app.add_url_rule(routes["eliminaru"], view_func=routes["eliminar_user_controllers"])
app.add_url_rule(routes["login"], view_func=routes["login_controllers"])
app.add_url_rule(routes["crear"], view_func=routes["crear_controllers"])
app.add_url_rule(routes["eliminar"], view_func=routes["eliminar_producto_controllers"])
app.add_url_rule(routes["productos"], view_func=routes["productos_controllers"])
app.add_url_rule(routes["productoId"], view_func=routes["productoId_controllers"])
app.add_url_rule(routes["cambioClave"], view_func=routes["cambioClave_controllers"])
app.add_url_rule(routes["ordenServicio"], view_func=routes["ordenServicio_controllers"])
app.add_url_rule(routes["consultaOrden"], view_func=routes["consultaOrden_controllers"])
app.add_url_rule(routes["asignacionTecnico"], view_func=routes["asignacionTecnico_controllers"])
app.add_url_rule(routes["consultaTecnicos"], view_func=routes["consultaTecnicos_controllers"])
app.add_url_rule(routes["tokenContrasena"], view_func=routes["tokenContrasena_controllers"])
app.add_url_rule(routes["consultaDiagnostico"],view_func=routes["consultaDiagnostico_controllers"])
app.add_url_rule(routes["consultaOrdenTecnicos"],view_func=routes["consultaOrdenTecnicos_controllers"])
app.add_url_rule(routes["consultaUsuario"],view_func=routes["consultaUsuario_controllers"])
app.add_url_rule(routes["actualizarUsuario"],view_func=routes["actualizarUsuario_controllers"])
app.add_url_rule(routes["buscarProductos"],view_func=routes["buscarProductos_controllers"])
app.add_url_rule(routes["actualizarHistoria"],view_func=routes["actualizarHistoria_controllers"])
app.add_url_rule(routes["consultaDispositivoOrden"],view_func=routes["consultaDispositivoOrden_controllers"])

from controllers import RegisterControllers
from controllers import LoginControllers
from controllers import CrearControllers
from controllers import EliminarProductoControllers
from controllers import EliminarUserControllers
from controllers import ProductosControllers
from controllers import ProductoIdControllers
from controllers import CambioClaveControllers
from controllers import OrdenServicioControllers
from controllers import AsignacionTecnicoControllers
from controllers import TokenContrasenaControllers
from controllers import ConsultaOrdenControllers
from controllers import ConsultaTecnicosControllers

routes = {"register": "/register", "register_controllers":RegisterControllers.as_view("register_api"),
"eliminaru": "/eliminaruser", "eliminar_user_controllers":EliminarUserControllers.as_view("eliminarUser_api"),
"login": "/login", "login_controllers":LoginControllers.as_view("login_api"),
"crear": "/crearproducto", "crear_controllers":CrearControllers.as_view("crearProducto_api"),
"eliminar": "/eliminarproducto", "eliminar_producto_controllers":EliminarProductoControllers.as_view("eliminarProducto_api"),
"productos": "/productos", "productos_controllers":ProductosControllers.as_view("productos_api"),
"productoId": "/productoId", "productoId_controllers":ProductoIdControllers.as_view("productoId_api"),
"ordenServicio": "/ordenServicio", "ordenServicio_controllers":OrdenServicioControllers.as_view("ordenServicio_api"),
"asignacionTecnico": "/asignacionTecnico", "asignacionTecnico_controllers":AsignacionTecnicoControllers.as_view("asignacionTecnico_api"),
"consultaTecnicos": "/consultaTecnicos", "consultaTecnicos_controllers":ConsultaTecnicosControllers.as_view("consultaTecnicos_api"),
"tokenContrasena": "/tokenContrasena", "tokenContrasena_controllers":TokenContrasenaControllers.as_view("tokenContrasena_api"),
"consultaOrden": "/consultaOrden", "consultaOrden_controllers":ConsultaOrdenControllers.as_view("consultaOrden_api"),
"cambioClave": "/cambioClave", "cambioClave_controllers":CambioClaveControllers.as_view("cambioClave_api")
}

from controllers import RegisterControllers
from controllers import LoginControllers
from controllers import CrearControllers
from controllers import EliminarProductoControllers
from controllers import EliminarUserControllers
from controllers import ProductosControllers
from controllers import ProductoIdControllers
from controllers import CambioClaveControllers
from controllers import OrdenServicioControllers
from controllers import TokenContrasenaControllers
from controllers import ConsultaOrdenControllers
from controllers import ConsultaTecnicosControllers
from controllers import ConsultaDiagnosticoControllers
from controllers import ConsultaOrdenTecnicosControllers
from controllers import ConsultaUsuarioControllers
from controllers import RegisterAdminControllers
from controllers import ActualizarUsuarioControllers
from controllers import ConsultaDispositivoOrdenControllers
from controllers import ActualizarHistoriaControllers
from controllers import ActualizarSalidaControllers
from controllers import ConsultaEquipoControllers
from controllers import ConsultaHistoricoUsuarioControllers
from controllers import ActualizarProductoControllers
from controllers import ConsultaEstadoOrdenControllers
from controllers import ProductosBuscarControllers

routes = {"register": "/register", "register_controllers":RegisterControllers.as_view("register_api"),
"registerAdmin": "/registerAdmin", "registerAdmin_controllers":RegisterAdminControllers.as_view("registerAdmin_api"),
"eliminaru": "/eliminaruser", "eliminar_user_controllers":EliminarUserControllers.as_view("eliminarUser_api"),
"login": "/login", "login_controllers":LoginControllers.as_view("login_api"),
"crear": "/crearproducto", "crear_controllers":CrearControllers.as_view("crearProducto_api"),
"eliminar": "/eliminarproducto", "eliminar_producto_controllers":EliminarProductoControllers.as_view("eliminarProducto_api"),
"productos": "/productos", "productos_controllers":ProductosControllers.as_view("productos_api"),
"productoId": "/productoId", "productoId_controllers":ProductoIdControllers.as_view("productoId_api"),
"consultaDiagnostico": "/consultaDiagnostico", "consultaDiagnostico_controllers":ConsultaDiagnosticoControllers.as_view("consultaDiagnostico_api"),
"ordenServicio": "/ordenServicio", "ordenServicio_controllers":OrdenServicioControllers.as_view("ordenServicio_api"),
"consultaTecnicos": "/consultaTecnicos", "consultaTecnicos_controllers":ConsultaTecnicosControllers.as_view("consultaTecnicos_api"),
"consultaUsuario": "/consultaUsuario", "consultaUsuario_controllers":ConsultaUsuarioControllers.as_view("consultaUsuario_api"),
"consultaEstadoOrden": "/consultaEstadoOrden", "consultaEstadoOrden_controllers":ConsultaEstadoOrdenControllers.as_view("consultaEstadoOrden_api"),
"tokenContrasena": "/tokenContrasena", "tokenContrasena_controllers":TokenContrasenaControllers.as_view("tokenContrasena_api"),
"consultaOrden": "/consultaOrden", "consultaOrden_controllers":ConsultaOrdenControllers.as_view("consultaOrden_api"),
"consultaOrdenTecnicos": "/consultaOrdenTecnicos", "consultaOrdenTecnicos_controllers":ConsultaOrdenTecnicosControllers.as_view("consultaOrdenTecnicos_api"),
"actualizarUsuario": "/actualizarUsuario", "actualizarUsuario_controllers":ActualizarUsuarioControllers.as_view("actualizarUsuarios_api"),
"cambioClave": "/cambioClave", "cambioClave_controllers":CambioClaveControllers.as_view("cambioClave_api"),
"consultaDispositivoOrden": "/consultaOrdenServicio", "consultaDispositivoOrden_controllers":ConsultaDispositivoOrdenControllers.as_view("consultaDispositivoOrden_api"),
"consultaEquipo": "/consultaEquipo", "consultaEquipo_controllers":ConsultaEquipoControllers.as_view("consultaEquipo_api"),
"actualizarHistoria": "/actualizarHistoria", "actualizarHistoria_controllers":ActualizarHistoriaControllers.as_view("actualizarHistoria_api"),
"consultaHistoria": "/consultaHistoria", "consultaHistoria_controllers":ConsultaHistoricoUsuarioControllers.as_view("consultaHistoria_api"),
"actualizarSalida": "/actualizarSalida", "actualizarSalida_controllers":ActualizarSalidaControllers.as_view("actualizarSalida_api"),
"actualizarProducto": "/actualizarProducto", "actualizarProducto_controllers":ActualizarProductoControllers.as_view("actualizarProducto_api"),
"buscarProductos": "/buscarProductos", "buscarProductos_controllers":ProductosBuscarControllers.as_view("buscarProductos_api")
}

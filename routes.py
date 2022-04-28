from controllers import RegisterControllers
from controllers import LoginControllers
#from controllers import CrearControllers
from controllers import ProductosControllers

routes = {"register": "/register", "register_controllers":RegisterControllers.as_view("register_api"),
"login": "/login", "login_controllers":LoginControllers.as_view("login_api"),
"productos": "/productos", "productos_controllers":ProductosControllers.as_view("productos_api")
}
# "crear": "/crearproducto", "crear_controllers":CrearControllers.as_view("crearProducto_api"),
# "productos": "/productos", "productos_controllers":ProductosControllers.as_view("productos_api"),

#}

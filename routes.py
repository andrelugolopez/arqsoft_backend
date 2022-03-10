from controllers import RegisterControllers, LoginControllers, JsonControllers, StockControllers

routes = {
"register": "/api/v01/register", "register_controllers": RegisterControllers.as_view("register_api"),
"login": "/api/v01/login", "login_controllers": LoginControllers.as_view("login_api"),
"json": "/api/v01/json", "json_controllers": JsonControllers.as_view("json_api"),
"stock": "/api/v01/stock", "stock_controllers": StockControllers.as_view("stock_api")
}

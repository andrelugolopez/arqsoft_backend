from flask import Flask
from routes import *
from flask_cors import CORS

app = Flask(__name__)
#llave con que se firmaran nuestras cookies de sesion
app.secret_key = "ARQSOFT_123"

CORS(app, resources={r"/*": {"origins": "*"}})


app.add_url_rule(routes["register"], view_func=routes["register_controllers"])
app.add_url_rule(routes["login"], view_func=routes["login_controllers"])
app.add_url_rule(routes["json"], view_func=routes["json_controllers"])
app.add_url_rule(routes["stock"], view_func=routes["stock_controllers"])

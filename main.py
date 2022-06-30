from app import app

PORT = 5000
DEBUG = True
HOST= "0.0.0.0"

app.run( host= HOST, port=PORT, debug=DEBUG)

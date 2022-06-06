import os
from flask import Flask
from flask_mysqldb import MySQL
from flask_cors import CORS

app=Flask(__name__)
# app.config['MYSQL_HOST'] = "mysql"
app.config['MYSQL_HOST'] = os.getenv('host-mysql')
# app.config['MYSQL_PASSWORD'] = "root"
app.config['MYSQL_PASSWORD'] = os.getenv('password-mysql')
app.config['MYSQL_DB'] = "modulos"

conexion=MySQL(app)

CORS(app)


def pagina_no_encontrada(error):
    return "error", 404

if __name__ == '__main__':
    # app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()

from unidades import un
from modulos import mod
app.register_blueprint(mod)
app.register_blueprint(un)
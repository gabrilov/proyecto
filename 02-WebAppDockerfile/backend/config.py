class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = '172.31.0.4'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'root'
    MYSQL_DB = 'modulos'
    # MYSQL_PORT = 3306

config = {
    'development': DevelopmentConfig
}
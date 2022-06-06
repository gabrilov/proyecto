from flask import Blueprint, jsonify, request

mod = Blueprint('modulos', __name__)
from app import conexion

@mod.get('/modulos')
def listar_modulos():
    try:
        cursor = conexion.connection.cursor()
        sql = 'SELECT * FROM modulos'
        cursor.execute(sql)
        datos = cursor.fetchall()
        modulos = []
        for fila in datos:
            modulo = {'id':fila[0], 'modulo':fila[1], 'url':fila[2]}
            modulos.append(modulo)
        return jsonify({'modulos':modulos, 'mensaje': 'Modulos listados'})
    except Exception as ex:
        print('-------------------------------------------------')
        print(ex)
        print('-------------------------------------------------')
        return jsonify({'mensaje': 'error', 'error': str(ex)})

@mod.get('/modulos/<id_modulo>')
def modulo(id_modulo):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM modulos WHERE id_modulo= '{0}'".format(id_modulo)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            modulo = {'id':datos[0], 'modulo':datos[1], 'url':datos[2]}            
            return jsonify({'modulo':modulo, 'mensaje': 'Modulo encontrado'})
        else:
            return jsonify({'mensaje': 'Este módulo no existe'})
    except Exception as ex:
        print('-------------------------------------------------')
        print(ex)
        print('-------------------------------------------------')
        return jsonify({'mensaje': 'error', 'error': str(ex)})

@mod.post('/modulo')
def registrar_modulo():
    try:
        cursor = conexion.connection.cursor()
        sql = """INSERT INTO modulos (id_modulo, modulo, url)
         VALUES ('{0}', '{1}', '{2}')""".format(request.json['id_modulo'], request.json['modulo'], request.json['url'])
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'mensaje': 'Registrado'})
    except Exception as ex:
        print('-------------------------------------------------')
        print(ex)
        print('-------------------------------------------------')
        return jsonify({'mensaje': 'error', 'error': str(ex)})

@mod.delete('/modulo/<id_modulo>')
def eliminar_modulo(id_modulo):
    try:
        cursor = conexion.connection.cursor()
        sql = "DELETE FROM modulos WHERE id_modulo= '{0}'".format(id_modulo)
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'mensaje': 'Registro borrado'})
    except Exception as ex:
        print('-------------------------------------------------')
        print(ex)
        print('-------------------------------------------------')
        return jsonify({'mensaje': 'error', 'error': str(ex)})

@mod.put('/modulo/<id_modulo>')
def actualizar_modulo(id_modulo):
    print(conexion)
    try:
        cursor = conexion.connection.cursor()
        sql = 'UPDATE modulos SET modulo="{0}", url="{1}" WHERE id_modulo="{2}"'.format(
                request.json['modulo'],
                request.json['url'],
                id_modulo
            )
        print(sql)
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'Resultado': 'Actualizado'})
    except Exception as ex:
        print('-------------------------------------------------')
        print(ex)
        print('-------------------------------------------------')
        return jsonify({'mensaje': 'error', 'error': str(ex)})
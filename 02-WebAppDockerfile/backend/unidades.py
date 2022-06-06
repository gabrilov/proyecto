from flask import Blueprint, jsonify, request

un = Blueprint('unidades', __name__)
from app import conexion

@un.get('/unidades')
def listar_unidades():
    try:
        cursor = conexion.connection.cursor()
        sql = 'SELECT * FROM unidades'
        cursor.execute(sql)
        datos = cursor.fetchall()
        unidades = []
        for fila in datos:
            unidad = {'id_modulo':fila[0], 'unidad':fila[1], 'titulo':fila[2]}
            unidades.append(unidad)
        return jsonify({'unidades':unidades, 'mensaje': 'Unidades listadas'})
    except Exception as ex:
        print('-------------------------------------------------')
        print(ex)
        print('-------------------------------------------------')
        return jsonify({'mensaje': 'error', 'error': str(ex)})

@un.get('/unidades/<id_modulo>/<unidad>')
def modulo(id_modulo, unidad):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM unidades WHERE id_modulo='{0}' and unidad={1}".format(id_modulo, unidad)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            result = {'id_modulo':datos[0], 'unidad':datos[1], 'titulo':datos[2]}            
            return jsonify({'unidad':result, 'mensaje': 'Unidad encontrada'})
        else:
            return jsonify({'mensaje': 'Este módulo no existe'})
    except Exception as ex:
        print('-------------------------------------------------')
        print(ex)
        print('-------------------------------------------------')
        return jsonify({'mensaje': 'error', 'error': str(ex)})

@un.post('/unidad')
def registrar_modulo():
    try:
        cursor = conexion.connection.cursor()
        sql = """INSERT INTO unidades (id_modulo, unidad, titulo)
         VALUES ('{0}', '{1}', '{2}')""".format(request.json['id_modulo'],request.json['unidad'], request.json['titulo'])
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'mensaje': 'Registrado'})
    except Exception as ex:
        print('-------------------------------------------------')
        print(ex)
        print('-------------------------------------------------')
        return jsonify({'mensaje': 'error', 'error': str(ex)})

@un.delete('/unidad/<id_modulo>/<unidad>')
def eliminar_modulo(id_modulo, unidad):
    try:
        cursor = conexion.connection.cursor()
        sql = "DELETE FROM unidades WHERE id_modulo='{0}' and unidad={1}".format(id_modulo, unidad)
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'mensaje': 'Registro borrado'})
    except Exception as ex:
        print('-------------------------------------------------')
        print(ex)
        print('-------------------------------------------------')
        return jsonify({'mensaje': 'error', 'error': str(ex)})

@un.put('/unidad/<id_modulo>/<unidad>')
def actualizar_modulo(id_modulo, unidad):
    try:
        cursor = conexion.connection.cursor()
        sql = 'UPDATE unidades SET titulo="{0}" WHERE id_modulo="{1}" and unidad={2}'.format(
                request.json['titulo'],              
                id_modulo,
                unidad
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
        
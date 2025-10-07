from flask import Flask, jsonify, request

app = Flask(__name__)

frutas = ['manzana', 'pera']

@app.route('/hello', methods=['GET'])
def decir_hola():
    return jsonify({'msg': 'POV: el esclavo de egipto desayunando 3 latigazos'}), 500

@app.route('/adios', methods=['GET'])
def decir_adios():
    return jsonify({'msg': 'Al final te has ido calentito.'})

@app.route('/frutas/<int:id_fruta>', methods=['GET'])
def recuperar_frutas(id_fruta):
    if id_fruta >= len(frutas):
        return jsonify({'msg': 'ese id de fruta no existe'}), 404
    fruta_escogida = frutas[id_fruta]
    return jsonify({'esta es tu fruta' : fruta_escogida })
# 

@app.route('/registro', methods=['POST'])
def register():
    body = request.get_json(silent=True)
    if body is None:
        return jsonify({'Debes enviar un body'}), 400
    # Para registrarse el usuario debe enviar email y password
    # debo asegurarme que el usuario en el body me envie el email y password
    if 'email' not in body:
        return jsonify({'msg': 'Campo Email es obligatorio'}), 400
    if 'password' not in body:
        return jsonify({'msg': 'Campo password es obligatori'}), 400
    body = request.get_json()
    print(body)
    return jsonify({'msg': 'Todo salio bien!', "data": body}), 201



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)


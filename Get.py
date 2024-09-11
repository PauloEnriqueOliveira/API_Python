from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
 
app = Flask(__name__)

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="endpoint",
            user="login",
            password="senha",
            database="banco"
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Erro na conexão ao banco de dados: {e}")
        return None

@app.route('/consulta', methods=['GET'])
def consulta_cpf():
    cb = request.args.get('coluna_de_busca')
    if not cb:
        return jsonify({"erro": "coluna_de_busca não fornecido"}), 400

    try:
        connection = create_connection()
        if connection is None:
            return jsonify({"erro": "Não foi possível conectar ao banco"}), 500

        cursor = connection.cursor(dictionary=True)
        
        query = "SELECT coluna_selecionada1, coluna_selecionada2 FROM tabela_selecionada WHERE coluna_de_busca = %s"
        cursor.execute(query, (cb,))
        resultado = cursor.fetchone()

        if resultado:
            return jsonify(resultado), 200
        else:
            return jsonify({"mensagem": "coluna_de_busca não encontrado"}), 404
    except Error as e:
        return jsonify({"erro": str(e)}), 500
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == '__main__':
    app.run(debug=True)

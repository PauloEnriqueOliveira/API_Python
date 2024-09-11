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
    

@app.route('/inserir_cpf', methods=['POST'])
def inserir_cpf():
    dados = request.json
    col1 = dados.get('coluna')
    col2 = dados.get('coluna2')

    if not all([col1, col2]):
        return jsonify({"erro": "Dados insuficientes. Por favor, forneça todos os campos necessários."}), 400

    try:
        connection = create_connection()
        if connection is None:
            return jsonify({"erro": "Não foi possível conectar ao banco"}), 500

        cursor = connection.cursor()
        query = "INSERT INTO tabela_fic (coluna, coluna2) VALUES (%s, %s)"
        cursor.execute(query, (col1, col2))
        connection.commit()

        return jsonify({"mensagem": "Coluna inserida com sucesso"}), 201
    except Error as e:
        return jsonify({"erro": str(e)}), 500
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == '__main__':
    app.run(debug=True)

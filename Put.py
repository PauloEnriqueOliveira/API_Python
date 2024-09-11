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
    
@app.route('/atualizar', methods=['PUT'])
def atualizar_cpf():
    dados = request.json
    col1 = dados.get('Coluna')
    col2 = dados.get('Coluna2')

    if not col1:
        return jsonify({"erro": "coluna não fornecido"}), 400

    try:
        connection = create_connection()
        if connection is None:
            return jsonify({"erro": "Não foi possível conectar ao banco"}), 500

        cursor = connection.cursor()
        query = "UPDATE Tabela_Selecionada SET Coluna2 = %s WHERE Coluna = %s"
        cursor.execute(query, (col2, col1))
        connection.commit()

        if cursor.rowcount == 0:
            return jsonify({"mensagem": "Coluna não encontrado"}), 404
        return jsonify({"mensagem": "Dados atualizados com sucesso"}), 200
    except Error as e:
        return jsonify({"erro": str(e)}), 500
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == '__main__':
    app.run(debug=True)                

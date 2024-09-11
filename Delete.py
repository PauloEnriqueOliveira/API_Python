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

@app.route('/deletar', methods=['DELETE'])
def deletar_cpf():
    col1 = request.args.get('coluna')

    if not col1:
        return jsonify({"erro": "Coluna não fornecida"}), 400

    try:
        connection = create_connection()
        if connection is None:
            return jsonify({"erro": "Não foi possível conectar ao banco"}), 500

        cursor = connection.cursor()
        query = "DELETE FROM tabela_selecionada WHERE coluna = %s"
        cursor.execute(query, (col1,))
        connection.commit()

        if cursor.rowcount == 0:
            return jsonify({"mensagem": "Coluna não encontrado"}), 404
        return jsonify({"mensagem": "Coluna deletada com sucesso"}), 200
    except Error as e:
        return jsonify({"erro": str(e)}), 500
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == '__main__':
    app.run(debug=True)

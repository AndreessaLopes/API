from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/dobro', methods=['POST'])
def dobro():
    # Obtém o valor enviado na requisição POST
    data = request.get_json()

    # Verifica se o campo 'valor' está presente na requisição
    if 'valor' not in data:
        return jsonify({'error': 'Campo "valor" ausente'}), 400

    # Obtém o valor a ser dobrado
    valor = data['valor']

    # Calcula o dobro do valor
    resultado = valor * 2

    # Retorna o resultado como JSON
    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    # Executa o aplicativo na porta 5000 por padrão
    app.run(debug=True)

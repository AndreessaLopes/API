from flask import Flask, request, jsonify
import base64

app = Flask(__name__)

@app.route('/processar_imagens', methods=['POST'])
def processar_imagens():
    # Obtém a lista de arquivos de imagem enviados na requisição
    imagens = request.files.getlist('imagens')

    if not imagens:
        return jsonify({'error': 'Nenhuma imagem recebida'}), 400

    resultados = ["ola"]

    for imagem in imagens:
        # Lê a imagem e converte para base64
        imagem_bytes = imagem.read()
        imagem_base64 = base64.b64encode(imagem_bytes).decode('utf-8')

        # Processa a imagem (aqui você pode fazer o que desejar com a imagem)
        # Neste exemplo, estamos apenas retornando a representação base64
        resultados.append(imagem_base64)

    # Retorna os resultados como strings em formato JSON
    return jsonify({'resultados': resultados})

if __name__ == '__main__':
    # Executa o aplicativo na porta 5000 por padrão
    app.run(debug=True)

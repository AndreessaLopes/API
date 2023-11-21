# Use a imagem base do Python
FROM python:3

# Configuração do diretório de trabalho
WORKDIR /usr/src/app

# Copie os arquivos de requisitos e instale as dependências
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código-fonte
COPY . .

# Comando para iniciar o servidor Flask
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]



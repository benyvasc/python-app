# Utiliza uma imagem leve do Python como base
FROM python:3.9-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo de código fonte para dentro do contêiner
COPY app.py .

# Instala a dependência necessária (Flask)
RUN pip install --no-cache-dir flask

# Expõe a porta 8080 para o mundo exterior
EXPOSE 8080

# Comando para rodar a aplicação
# Alteramos o comando para que o Flask escute na porta 8080 internamente
CMD ["python", "app.py"]
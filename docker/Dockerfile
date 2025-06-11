FROM python:3.10-slim

WORKDIR /app

# Copia a pasta da aplicação para dentro do container
COPY ../app /app

# Instala as dependências
RUN pip install grpcio grpcio-tools pika

# Expõe a porta do gRPC
EXPOSE 50051

# Comando padrão
CMD ["python", "server.py"]

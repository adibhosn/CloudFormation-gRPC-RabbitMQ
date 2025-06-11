# Sistema Distribuído com gRPC, RabbitMQ e Docker. Feito com o intuito de ser usado no CloudFormation da AWS

## Tecnologias
- Python
- gRPC
- RabbitMQ
- CloudFormation (AWS)
- Docker

## Como Rodar Local

```bash
# Inicializar Docker
docker-compose up --build
````
# Em outro terminal Testar gRPC
python app/client.py

# Enviar mensagens
python app/queue_sender.py

# Rodar worker
python app/worker.py

# Cloud Formation:
Basta subir o arquivo Yaml presente na pasta "cloudformation", que uma ec2 será criada, (não esqueça de editar para sua key e versão de AMI que deseja usar)

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='tasks')

for i in range(10):
    message = f"Task {i}"
    channel.basic_publish(exchange='', routing_key='tasks', body=message)
    print(f" [x] Sent {message}")

connection.close()

import pika


credentials = pika.PlainCredentials(username='admin', password='admin1')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq',port=5672,credentials=credentials)) 

channel = connection.channel()
print("started consumer")

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print("receive admin")
    print(" [x] Received %r" % body)

print("started consumer1")

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)
print("started consuming")
channel.start_consuming()

channel.close()
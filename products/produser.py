import pika

credentials = pika.PlainCredentials(username='admin', password='admin1')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq',port=5672,credentials=credentials)) 

channel = connection.channel()
print("start produser py")
def publish():
    channel.basic_publish(exchange="", routing_key='admin', body='hello')
    print("start produser")

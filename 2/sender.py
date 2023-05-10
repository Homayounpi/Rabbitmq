import pika

conection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

ch=conection.channel()

ch.queue_declare(queue='first',durable=True)

messages='Thes is a Testing masseges!!!'


ch.basic_publish(exchange='',routing_key='first',body=messages,
                 properties=pika.BasicProperties(delivery_mode=2,headers={'name':'amir'}))

print('send messeges!!!')

conection.close()


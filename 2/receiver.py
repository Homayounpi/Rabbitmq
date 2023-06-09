import pika
import time
# import ce

connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

ch=connection.channel()

ch.queue_declare(queue='first',durable=True)

print('Weiting for massage . press ctrl+C exit')
def callback(ch,method,properties,body) :
    print(f'Received {body}')
    # print(properties.headers['name'])
    print(properties.headers)
    print(method)
    time.sleep(4)
    print('done')
    ch.basic_ack(delivery_tag=method.delivery_tag)

ch.basic_qos(prefetch_count=1)
ch.basic_consume(queue='first',on_message_callback=callback)

ch.start_consuming()
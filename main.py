# import pika
#
# connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.1.28'))
# channel = connection.channel()
# channel.exchange_declare(exchange='test-exchange', exchange_type='direct')
# result = channel.queue_declare(exclusive=True)
# queue_name = result.method.queue
# channel.queue_bind(exchange='test-exchange', queue=queue_name)
#
# print("___ waiting for message")
#
# def callback (ch, method, properties, body) :
#     print("[x] %r" %body)
#
# channel.basic_consume(callback, queue=queue_name, no_ack=True)
#
# channel.start_consuming()

########################################################################################################################

# import pika
#
# QUEUE_NAME = 'test-queue'
# # RabbitMQ Server Connection 생성
# connection = pika.BlockingConnection(pika.URLParameters('amqp://sohyun:5050@192.168.1.28:5672/'))
#
# # RabbitMQ Server 와 통신 하기 위한 channel 생성
# channel = connection.channel()
#
# # Message Queue 생성
# # Consumer가 먼저 실행될 경우 접근할 Queue가 없기 때문에 생성
# channel.queue_declare(queue=QUEUE_NAME)
#
# # 메시지를 받으면 실행할 task(함수)를 정의합니다.
# def callback(ch, method, properties, body):
#     print(" [x] Received %r" % body)
#     ch.basic_ack( delivery_tag=method.delivery_tag )
#
# # consumer로 설정하여 queue로 부터 메시지를 받아 task를 수행할 수 있도록 합니다.
# # channel.basic_qos(prefetch_count=1)
# channel.basic_consume(QUEUE_NAME, callback)
#
# print(' [*] Waiting for messages. To exit press CTRL+C')
# channel.start_consuming()

########################################################################################################################

import pika
class Main:
    def __init__(self):
        self.url = '192.168.1.28'
        self.port = 5672
        self.vhost = '/'
        self.cred = pika.PlainCredentials('sohyun', '5050')
        self.queue = 'test-queue'
        return

    def on_message(ch, method, header, body):
        print("received %s" %body)
        return
    def main(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(self.url, self.port, self.vhost, self.cred))
        channel = connection.channel()
        channel.basic_consume(
            queue=self.queue
            , on_message_callback=Main.on_message
            , auto_ack=True
        )
        print("Consumer is starting ... ")
        channel.start_consuming()
        return
consumer =  Main()
consumer.main()
import pika
import json

from part_II.confirmation import send_confirmation_sms, send_confirmation_email, set_contact_as_confirmed


def consumer(queue_name):
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name, durable=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        message = json.loads(body.decode())
        print(send_confirmation_sms(message['id'], message['contact']) if queue_name == 'phone'
              else send_confirmation_email(message['id'], message['contact']))
        print(set_contact_as_confirmed(message['id']))
        ch.basic_ack(delivery_tag=method.delivery_tag)
        print(f" [x] All done for contact with the ID: {message['id']}")

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=queue_name, on_message_callback=callback)

    channel.start_consuming()

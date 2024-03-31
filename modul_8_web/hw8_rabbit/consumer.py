import pika
from mongoengine import connect, Document, StringField, BooleanField
from bson import ObjectId
import time

# Підключення до MongoDB
connect('email_contacts')

# Визначення моделі контакту
class Contact(Document):
    full_name = StringField(required=True)
    email = StringField(required=True)
    sent = BooleanField(default=False)

# Функція для імітації надсилання email
def send_email(contact_id):
    contact = Contact.objects.get(id=ObjectId(contact_id))
    print(f"Sending email to {contact.email}...")
    # Тут можна додати логіку надсилання реального email
    # Після надсилання встановлюємо логічне поле sent в True
    contact.sent = True
    contact.save()
    print("Email sent successfully!")

# Функція для обробки повідомлень з черги RabbitMQ
def callback(ch, method, properties, body):
    print(f"Received message: {body}")
    send_email(body.decode())
    print("Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

# Підключення до RabbitMQ та створення каналу
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Створення черги
channel.queue_declare(queue='email_queue')

# Обробка повідомлень з черги
channel.basic_consume(queue='email_queue', on_message_callback=callback)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()


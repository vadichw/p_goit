import pika
from mongoengine import connect, Document, StringField, BooleanField
from bson import ObjectId
import faker

# Підключення до MongoDB
connect('email_contacts')

# Визначення моделі контакту
class Contact(Document):
    full_name = StringField(required=True)
    email = StringField(required=True)
    sent = BooleanField(default=False)

# Функція для створення фейкових контактів
def create_fake_contacts(num_contacts):
    fake = faker.Faker()
    contacts = []
    for _ in range(num_contacts):
        full_name = fake.name()
        email = fake.email()
        contact = Contact(full_name=full_name, email=email)
        contact.save()
        contacts.append(contact)
    return contacts

# Підключення до RabbitMQ та створення каналу
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672))
channel = connection.channel()

# Створення черги
channel.queue_declare(queue='email_queue')

# Генерація фейкових контактів та їх запис у базу даних
contacts = create_fake_contacts(10)

# Відправка повідомлень у чергу RabbitMQ
for contact in contacts:
    message = str(contact.id)
    channel.basic_publish(exchange='', routing_key='email_queue', body=message)
    print(f"Sent message with ObjectID: {contact.id}")

# Закриття з'єднання з RabbitMQ
connection.close()


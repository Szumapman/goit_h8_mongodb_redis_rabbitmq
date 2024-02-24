from random import choice
import json

import faker
import pika

from part_II.models import Contact
from part_I.connect import connect


NUMBER_OF_CONTACTS = 10


def seed_fake_contacts(number_of_contacts):
    fake = faker.Faker("pl_PL")
    for _ in range(number_of_contacts):
        firstname: str = fake.first_name()
        lastname: str = fake.last_name()
        Contact(
            firstname=firstname,
            lastname=lastname,
            email=f"{firstname.lower()}.{lastname.lower()}@{fake.free_email_domain()}",
            phone=fake.phone_number(),
            preferred_contact_channel=choice(["email", "phone"]),
        ).save()


def publish():
    contacts = Contact.objects(is_confirmed=False)
    credentials = pika.PlainCredentials("guest", "guest")
    with pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials)) as connection:
        channel = connection.channel()
        channel.exchange_declare(exchange="task_confirmation_mock", exchange_type="direct")
        channel.queue_declare(queue="email", durable=True)
        channel.queue_bind(exchange="task_confirmation_mock", queue="email")
        channel.queue_declare(queue="phone", durable=True)
        channel.queue_bind(exchange="task_confirmation_mock", queue="phone")
        channel.confirm_delivery()

        for contact in contacts:
            message = {
                "id": str(contact.id),
                "contact": contact.email if contact.preferred_contact_channel == "email" else contact.phone
            }
            try:
                channel.basic_publish(
                    exchange="task_confirmation_mock",
                    routing_key=contact.preferred_contact_channel,
                    body=json.dumps(message).encode(),
                    properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE),
                )
            except pika.exceptions.UnroutableError:
                print(f" [!] Error while sending message to contact id: {contact.id} via ",
                      contact.email if contact.preferred_contact_channel == "email" else contact.phone)


if __name__ == "__main__":
    seed_fake_contacts(NUMBER_OF_CONTACTS)
    publish()

from part_II.models import Contact
from part_I.connect import connect


def send_confirmation_sms(id, phone):
    return f" [x] Sending confirmation message to contact {id} at phone number: {phone}"


def send_confirmation_email(id, email):
    return f" [x] Sending confirmation message to contact {id} at email: {email}"


def set_contact_as_confirmed(id):
    contact = Contact.objects(id=id).first()
    contact.is_confirmed = True
    contact.save()
    return f" [x] Set contact {id} as confirmed"

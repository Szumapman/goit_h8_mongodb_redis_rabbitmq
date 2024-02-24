from mongoengine import Document
from mongoengine.fields import StringField,BooleanField


class Contact(Document):
    firstname = StringField(required=True)
    lastname = StringField(required=True)
    email = StringField(max_length=255, required=True)
    phone = StringField(max_length=30)
    preferred_contact_channel = StringField(max_length=5, default="email", choices=["email", "phone"], required=True)
    is_confirmed = BooleanField(default=False)
    meta = {"allow_inheritance": True}


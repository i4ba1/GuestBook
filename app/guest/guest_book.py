from app.db import db


class GuestBook(db.Document):
    firstName = db.ListField(db.StringField(), required=True)
    lastName = db.ListField(db.StringField(), required=True)
    fullName = db.ListField()
    email: db.ListField(required=True, unique=True)
    mobilePhone: db.ListField(required=True, unique=True)
    purpose: db.ListField(db.StringField(), required=True)
    meetWho: db.ListField(db.StringField(), required=True)
    pictureUrl: db.ListField(db.StringField(), required=True)
    captcha: db.ListField(db.StringField(), required=True)

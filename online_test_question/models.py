from online_test.extensions import db


class Question(db.Document):
    title = db.StringField(required=True, min_length=5, max_length=100)
    description = db.StringField(required=True, min_length=5)
    multiple_answers = db.BooleanField(default=False)
    order = db.IntField(required=True, default=1, min_value=1)

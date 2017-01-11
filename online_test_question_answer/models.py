from online_test.extensions import db


class QuestionAnswer(db.Document):
    text = db.StringField(required=True, min_length=5, max_length=100)
    order = db.IntField(required=True, default=1, min_value=1)
    correct_choice = db.BooleanField(required=True, default=False)

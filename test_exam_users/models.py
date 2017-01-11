from test_exam.extensions import db
from test_exam_util.constants import MongoEngine, User as UserC


class User(db.Document):
    meta = {
        MongoEngine.INDEXES: [
            {
                MongoEngine.FIELDS: [UserC.USERNAME]
            }
        ],
    }

    full_name = db.StringField(required=True, min_length=5, max_length=100)
    username = db.StringField(required=True, unique=True, min_length=3, max_length=15)
    password = db.StringField(required=True, min_length=6, max_length=15, password=True)

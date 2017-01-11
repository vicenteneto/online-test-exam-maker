from online_test.extensions import db
from online_test_util.constants import MongoEngine, TestExam as TestExamC


class TestExam(db.Document):
    meta = {
        MongoEngine.INDEXES: [
            {
                MongoEngine.FIELDS: [TestExamC.NAME]
            }
        ],
    }

    name = db.StringField(required=True, unique=True, min_length=5, max_length=50)
    description = db.StringField(min_length=5)
    pass_score = db.IntField(required=True, min_value=1)
    total_score = db.IntField(required=True, min_value=1)
    duration = db.IntField(required=True, default=1, min_value=1)

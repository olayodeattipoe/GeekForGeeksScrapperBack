from main import db, app
from sqlalchemy.orm import sessionmaker

tables = ['social_studies', 'ad-on', 'BioC1hem']

engine = db.create_engine(
    "mysql://root:bolatito224@localhost:3306/learnhub")

Session = sessionmaker(bind=engine)
session = Session()


class BaseClass(db.Model):
    __abstract__ = True
    # I'd : Field which stores unique id for every row in
    # database table.
    # first_name: Used to store the first name if the user
    # last_name: Used to store last name of the user
    # Age: Used to store the age of the user
    id = db.Column(db.Integer, primary_key=True)
    Question = db.Column(db.Text, unique=False, nullable=False)
    Options = db.Column(db.Text, unique=False, nullable=False)
    Correct_Answer = db.Column(db.Text, nullable=False)
    Comment = db.Column(db.Text, nullable=True)


def create_table(table_name, data_set):
    entries = []

    class BaseClass1(BaseClass):
        __tablename__ = table_name

    if table_name is not tables:
        with app.app_context():
            db.create_all()

    # logic to extract formats
    for items in data_set:
        entries.append(BaseClass1(Question=items['Question'],
                                  Options=items['Options'],
                                  Correct_Answer=items['Correct_Answer'],
                                  Comment=items['Comment']))
    with app.app_context():
        db.session.bulk_save_objects(entries)
        db.session.commit()


def fetch(start):

    container = []

    class BaseClass1(BaseClass):
        __tablename__ = "python"

    result = session.query(BaseClass1.Question)

    result = result.add_columns(BaseClass1.Options,BaseClass1.Correct_Answer,BaseClass1.Comment)

    for r in result[start:start+5]:
        b2b = {
            'Question': r.Question,
            'Options': r.Options,
            'Correct_Answer': r.Correct_Answer,
            'Comment': r.Comment
        }
        container.append(b2b)
    return container

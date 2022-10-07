from xml.dom import ValidationErr
import sparrow
from json import load
from os import path
from rich import print

_test_data = path.abspath(path.join(path.dirname(__file__), "project-dump.json"))


@sparrow.task(name="load-test-data")
def load_test_data():
    db = sparrow.get_database()
    data = load(open(_test_data))
    print(data)
    try:
        db.load_data("project", data)
    except Exception as e:
        print("Exception: ", e)


@sparrow.task()
def log_sessions():
    db = sparrow.get_database()
    sessions = db.session.query(db.model.session).all()
    for session in sessions:
        print(session.uuid)

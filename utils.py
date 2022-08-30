from uuid import uuid4
from tools import db_orch as db


def create_db_tables(app):
    # create tables unless they exist
    from plugins.kanban.models.attachment import Attachment
    with app.app_context():
        db.create_all()
        db.session.commit()


def make_unique_filename(name):
    prefix = uuid4().__str__()
    return f"{prefix}-{name}"
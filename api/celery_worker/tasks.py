from celery import Task

from .celery import app
from db.database import db_session
from settings import get_settings


app_settings = get_settings()

NOTIFICATION_EMAIL = app_settings.notification_email


class SQLAlchemyTask(Task):
    """
    An abstract Celery Task that ensures that the connection the
    database is closed on task completion
    """
    abstract = True

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        db_session.remove()


@app.task(name="scraping", base=SQLAlchemyTask)
def scraping():
    try:
        pass
        # call your scraping functions here
    except Exception as e:
        pass
        # notifications here

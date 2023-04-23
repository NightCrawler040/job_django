import os

from celery.schedules import crontab

from ..django import TIME_ZONE as DJANGO_TIME_ZONE
from ..environment import env


CELERY_TASK_ALWAYS_EAGER = env.bool("SRC_CELERY_TASK_ALWAYS_EAGER", default=False)
CELERY_BROKER_URL = os.environ.get(
    "CELERY_BROKER",
    default="rediss://default:AVNS_gV2m6knwILZ7c7PRKq9@django-"
            "channels-redis-do-user-12147762-0.b.db.ondigitalocean.com:25061"
)

CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = DJANGO_TIME_ZONE

CELERY_BEAT_SCHEDULE = {
    "reservation_announce": {
        "task": "src.apps.partners.tasks.announce_reservations",
        "schedule": crontab(minute='*/1'),
    },
    "retract_announce_reservations": {
        "task": "src.apps.partners.tasks.retract_announce_reservations",
        "schedule": crontab(minute='*/1'),
    },
    "not_enough_balance": {
        "task": "src.apps.partners.tasks.not_enough_balance",
        "schedule": crontab(minute='*/1'),
    },
    "create_game_center_rates": {
        "task": "src.apps.partners.tasks.create_game_center_rates",
        "schedule": crontab(hour='*/1'),
    },
    "google_sheet_temp_task": {
        "task": "src.apps.partners.tasks.google_sheet_temp_task",
        "schedule": crontab(hour='*/1'),
    }
}

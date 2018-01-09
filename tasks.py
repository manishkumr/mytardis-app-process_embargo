from datetime import date
import datetime

from celery import task

from django.utils.timezone import localtime
from django.db import transaction

from ansto.tardis.utils.ingestion import acquire_lock
from ansto.tardis.utils.ingestion import release_lock

from tardis.tardis_portal.models import Experiment

@task(name="tardis_portal.process_embargo", ignore_result=True)
def process_embargo():
    exps = Experiment.objects.filter(public_access=Experiment.PUBLIC_ACCESS_NONE)
    today = date.today()
    for exp in exps:
        if acquire_lock(str(exp.id)):
            try:
                with transaction.atomic():
                    end_time = exp.end_time
                    if end_time is None:
                        continue
                    local_end_date = localtime(end_time).date()
                    experiment_age = today - local_end_date
                    if experiment_age > datetime.timedelta(days=1095):
                        exp.public_access = Experiment.PUBLIC_ACCESS_FULL
                        exp.save()
            finally:
                release_lock(str(exp.id))

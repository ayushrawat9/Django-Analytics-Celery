from celery import shared_task
from .models import PackageInfo
import requests


@shared_task(bind = True)
def updatedb(self):
    res = requests.get('https://s3.us-east-2.wasabisys.com/akshit/dataset-django/ft_assignment.json')
    res = res.json()
    for item in res:
        p = PackageInfo.objects.get(app_name = item["app_name"])
        p.package_id=item["package_id"]
        p.date_wise_metrics = item["date_wise_metrics"]
        p.save()
    return "Done"
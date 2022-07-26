from celery import shared_task
from .models import PackageInfo
import requests


@shared_task(bind = True)
def updatedb(self):
    res = requests.get('https://s3.us-east-2.wasabisys.com/akshit/dataset-django/ft_assignment.json')
    res = res.json()
    for item in res:
        try:
            obj = PackageInfo.objects.get(app_name = item["app_name"])
        except PackageInfo.DoesNotExist:
            obj= PackageInfo.objects.create(app_name = item["app_name"])
        obj.package_id=item["package_id"]
        obj.date_wise_metrics = item["date_wise_metrics"]
        obj.save()
    return "Done"
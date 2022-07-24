from operator import imod
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
import json
import requests
from .models import PackageInfo
from datetime import datetime
from dateutil import parser
import collections
# Create your views here.

def test(request):
    res = requests.get('https://s3.us-east-2.wasabisys.com/akshit/dataset-django/ft_assignment.json')
    res = res.json()
    # for item in res[:3]:
    #     for date_name,info in item["date_wise_metrics"].items():
    #         for date,datesv in info.items():
    #             # package = PackageInfo.objects.create(package_id=, price=1000, weight=200)
    #             date1 = datetime.strptime(date, "%d-%m-%Y")
    #             date1 = date1.date()
    #             package = PackageInfo.objects.create()
    #             print(item["package_id"],item["app_name"],date_name,date1,datesv)
    s=set()
    l=[]
    for item in res:
        s.add(item["package_id"])
        l.append(item['package_id'])
    frequency = collections.Counter(l)
    print(frequency )
    print(len(s))
    print(len(res))
    for item in res:
        p = PackageInfo.objects.create(package_id=item["package_id"],
                                        app_name=item["app_name"],
                                        date_wise_metrics = item["date_wise_metrics"])
        p.save()
    return HttpResponse("Done")

def get_data(request):
    if request.method == "POST":
        app_name =  request.POST["app_name"]
        from_date = request.POST["from"]
        to_date = request.POST["to"]
        from_date = parser.parse(from_date).date()
        to_date = parser.parse(to_date).date()
        try:
            dates = PackageInfo.objects.filter(app_name=app_name).values('date_wise_metrics')
        except Exception as e:
            print(e)

        dates = [date for date in dates]
        # dates = json.loads(dates)
        response = {}
        
        for date,date_values in dates[0].items():
            for item,value in date_values.items():
                response[item] = value

        xdata = []
        ydata = []
        
        from plotly.offline import plot
        from plotly.graph_objs import Scatter
        for items,value in response.items():
            x1=[]
            y1=[]
            for k,v in value.items():
                k1=parser.parse(k).date()
                if k1>=from_date and k1<=to_date:
                    x1.append(k)
                    y1.append(v)
            xdata.append(x1)
            ydata.append(y1)

        xdatat=[]
        # print(xdata)
        for data in xdata:
            temp=[]
            for date in data:
                date_new = parser.parse(date).date()
                print(date_new)
                temp.append(date_new)
            xdatat.append(temp)
        xdata=xdatat.copy()

        plot_div1 = plot([Scatter(x=xdata[0], y=ydata[0],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
        plot_div2 = plot([Scatter(x=xdata[1], y=ydata[1],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
        plot_div3 = plot([Scatter(x=xdata[2], y=ydata[2],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
        

        return render(request, "base.html",context={'plot_div1': plot_div1,
                                                    'plot_div2': plot_div2,
                                                    'plot_div3': plot_div3})

    return render(request, "base.html")

# AJAX
def load_app_name(request):
    app_name = PackageInfo.objects.all().values("app_name")
    #return render(request, 'appname_options.html', {'app_name': app_name})
    return JsonResponse(list(app_name), safe=False)
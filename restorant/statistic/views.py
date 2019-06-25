from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
import json
from django.conf import settings
from statistic.serializers import ReportSerializer
from datetime import datetime


def home(request):
    context = {}
    fecha = []
    count = 0
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        name_file = fs.save(myfile.name, myfile)
        context['url'] = fs.url(name_file)
        a = read_file(name_file)
        context['a'] = a
        esta = False
        for i in a:
            if count > 10:
                break
            if len(fecha) == 0:
                fecha.append({'fecha': str(i['date_closed'][:-9]), 'total': i['total']})
                continue
            for fe in fecha:
                if i['date_closed'][:-9] not in fe['fecha']:
                    esta = False
                else:
                    esta = True
                    break
            if esta == False:
                fecha.append({'fecha': str(i['date_closed'][:-9]), 'total': i['total']})
            else:
                fe['total'] = fe['total'] + i['total']
            context['total_dia'] = fecha
            count += 1

        return render(request, 'statistic/home.html', context)

    return render(request, 'statistic/home.html')

def read_file(f):
    with open('{}/{}'.format(settings.MEDIA_ROOT, f)) as f:

        data = json.load(f)
        data_data = []
        for d in data:
            serializer = ReportSerializer(d)
            data_data.append(serializer.data)
        return data_data

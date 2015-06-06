from django.shortcuts import render
from django.http import JsonResponse

from sensor_data. models import SensorReading
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def time_series(request):
    if request.method == 'GET':
        qs_reading = SensorReading.objects.all()
        response = {r.timestamp: r.reading for r in qs_reading}
        return JsonResponse(response)

    elif request.method == 'POST':
        reading = request.POST.get('reading')
        obj = SensorReading(reading=reading)
        obj.save()
        return JsonResponse({'status':'ok'})


from django.shortcuts import render
from .models import Content, Searches
import matplotlib.pyplot as plt
import matplotlib
import io
import urllib, base64

from django.shortcuts import render
from library.services.factory import create_statistics_service

# Create your views here.

def mental_health_library(request):
    topic = request.GET.get('topic')  # Obtenemos el tema seleccionado del formulario
    if topic:
        contents = Content.objects.filter(topic=topic)
        search = Searches(choice=topic)
        search.save()
    else:
        contents = Content.objects.all()

    context = {
        'contents': contents,
        'selected_topic': topic,
    }
    return render(request, 'library.html', context)


def search_statistics(request):
    service = create_statistics_service()
    topics = ['stress', 'depression', 'anxiety']
    data = service.get_search_counts(topics)
    graphic = service.generate_bar_chart(data)
    return render(request, 'statistics.html', {'graphic': graphic})

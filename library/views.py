from django.shortcuts import render
from .models import Content

# Create your views here.

def mental_health_library(request):
    topic = request.GET.get('topic')  # Obtenemos el tema seleccionado del formulario
    if topic:
        contents = Content.objects.filter(topic=topic)
    else:
        contents = Content.objects.all()

    context = {
        'contents': contents,
        'selected_topic': topic,
    }
    return render(request, 'library.html', context)

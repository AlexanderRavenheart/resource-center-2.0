from django.http import HttpResponse
from django.template import loader

def index(request):
    greeting = 'Hello!'
    template = loader.get_template('main/index.html')
    context = {
        'greeting': greeting,
    }
    return HttpResponse(template.render(context, request))

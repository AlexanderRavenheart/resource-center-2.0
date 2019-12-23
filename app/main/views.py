from django.http import HttpResponse
from django.template import loader

def home(request):
    template = loader.get_template('main/page/home.html')
    
    # scObject = Screenshots.objects.filter(ex_name="maps").order_by('-posted')[0:5]

    context = {
        # 'screenshots': scObject,
    }
    return HttpResponse(template.render(context, request))

def contacts(request):
    template = loader.get_template('main/page/contacts.html')
    context = {
        'title': 'Contacts',
    }
    return HttpResponse(template.render(context, request))

def faq(request):
    template = loader.get_template('main/page/faq.html')
    context = {
        'title': 'FAQ',
    }
    return HttpResponse(template.render(context, request))

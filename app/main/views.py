from django.http import HttpResponse
from django.template import loader
from urllib.parse import urlencode
import urllib.request
from main import send_email

def home(request):
    # scObject = Screenshots.objects.filter(ex_name="maps").order_by('-posted')[0:5]

    template = loader.get_template('main/page/home.html')
    context = {
        # 'screenshots': scObject,
    }
    return HttpResponse(template.render(context, request))


def contact(request):
    message_sent = False
    if request.method == 'POST':
        if request.POST.get('contacts_submit', "").strip() != "":
            name = request.POST.get('name', "")
            email = request.POST.get('email', "")
            message = request.POST.get('message', "")

            g_recaptcha_response = request.POST.get('g-recaptcha-response', "")
            if g_recaptcha_response:
                params = urlencode({
                    'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                    'response': g_recaptcha_response,
                    'remoteip': request.META.get("REMOTE_ADDR", ""),
                }).encode('utf-8')
                req = urllib.request.Request(
                    url="https://www.google.com/recaptcha/api/siteverify",
                    data=params,
                    headers={
                        "Content-type": "application/x-www-form-urlencoded",
                        "User-agent": "reCAPTCHA Python"
                    }
                )
                resp = urllib.request.urlopen(req).read().decode('utf-8')
                json_resp = json.loads(resp)
                if json_resp['success']:
                    send_email.send_email_contacts_form(name, email, message)
                    return HttpResponse('/contact/sent')
            return HttpResponse('/contact')

    template = loader.get_template('main/page/contact.html')
    context = {
        'title': 'Contact',
        'message_sent': message_sent,
    }
    return HttpResponse(template.render(context, request))


def contact_sent(request):
    message_sent = True

    template = loader.get_template('main/page/contact.html')
    context = {
        'title': 'Message sent',
        'message_sent': message_sent,
    }
    return HttpResponse(template.render(context, request))


def faq(request):
    template = loader.get_template('main/page/faq.html')
    context = {
        'title': 'FAQ',
    }
    return HttpResponse(template.render(context, request))

# Create your views here.
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from testapp.models import Publisher
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def hello(request):
    '''print(request.META.items())
   
    p1 = Publisher(name='Apress', address='2855 Telegraph Avenue',
                   city='Berkeley', state_province='CA', country='U.S.A.',
                   website='http://www.apress.com/')
    p1.save()
    return HttpResponse(request.META["HTTP_USER_AGENT"])
    '''
    return redirect('/current_datetime/')

def hello2(request, offset):
    #offset = int(offset)
    #print(offset)
    
    return HttpResponse("fc")


def search_form(request):
    return render_to_response('search_form.html')


def search(request):
    print("comes here")
    if 'q' in request.GET:
            print(request.GET)
            message = 'You searched for: %r' % request.GET['q']
    else:
            print("nothing get")
            message = 'You submitted an empty form.'
    return HttpResponse(message)

def contact_form(request):
    return render_to_response('contact_form.html')

def contact(request):
    errors = []
    print("test1")
    if request.method == 'GET':
        print("test1")
        print(request.GET)
        return HttpResponseRedirect('/thanks/')
    return render_to_response('contact_form.html')
        #{'errors': errors})

def thanks(request):
    print("fuck")
    return render_to_response('thanks.html')

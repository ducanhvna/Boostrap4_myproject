from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.template import loader

def index(request):
    template = loader.get_template('pools/index.html')
    context = {
        'latest_question_list': [],
    }
    return HttpResponse(template.render(context, request))


from django.views.generic import CreateView
from .models import Person

class PersonCreateView(CreateView):
    model = Person
    fields = ('name', 'email', 'job_title', 'bio')

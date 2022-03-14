from django.shortcuts import render

from project.models import SampleModel


def index(request):
    ctx = {}
    return render(request, template_name='index.html', context=ctx)


def sample_page(request):
    ctx = {
        'sample_context': "This message is just a sample context. It's set in python on project/views.py"
    }
    return render(request, template_name='sample_page.html', context=ctx)


def sample_page2(request):
    ctx = {
        'items': SampleModel.objects.all()
    }
    return render(request, template_name='sample_page2.html', context=ctx)

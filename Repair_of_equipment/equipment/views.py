from django.http import HttpResponse
from django.shortcuts import render
from equipment.models import Machine


def index_view(request):
    template = 'equipment/index.html'
    context = {}
    return render(request, template, context)

def equipment_view(request):
    template = 'equipment/list_machine.html'
    object_list = Machine.objects.all().prefetch_related('general')
    context = {'object_list': object_list}
    return render(request, template, context)

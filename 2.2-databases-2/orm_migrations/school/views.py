from django.views.generic import ListView
from django.shortcuts import render

from .models import Students, Teachers


def students_list(request):
    template = 'school/students_list.html'
    context = {'object_list': Students.objects.order_by('group'), 'teachers': Teachers.objects.all()}
    ordering = 'group'
    return render(request, template, context)

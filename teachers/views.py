from django.shortcuts import render
from .models import Teacher

# Create your views here.
# Teachers views

from django.views.generic import ListView

class TeachersView(ListView):
    template_name = 'teacher.html'
    queryset = Teacher.objects.all()
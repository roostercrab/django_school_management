from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Student
# Create your views here.

from django.views.generic import ListView

class HomeView(ListView):
    template_name = 'home.html'
    queryset = Student.objects.all()

    #def dispatch(self, *args, **kwargs):
        #return super(HomeView, self).dispatch(*args, **kwargs)
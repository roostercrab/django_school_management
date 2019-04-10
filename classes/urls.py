from django.urls import path
from .views import ClassView

urlpatterns = [
    path('classes',ClassView.as_view(),name='classpage')
]
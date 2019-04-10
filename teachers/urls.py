from django.urls import path
from .views import TeachersView

urlpatterns = [
    path('teachers',TeachersView.as_view(),name='teachers-list')
]
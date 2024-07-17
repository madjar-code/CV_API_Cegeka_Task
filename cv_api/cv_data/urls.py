from django.urls import path
from . import views

urlpatterns = [
    path('personal/', views.personal_view, name='personal'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('personal/', views.personal_view, name='personal'),
    path('experience/', views.experience_view, name='experience'),
    path('education/', views.education_view, name='education'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create-entry/', views.CreateEntryView.as_view(), name='create-entry'),
    path('delete/<str:pk>/', views.deleteEntry, name='delete'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('entry-list/', views.entryList, name='entry-list'),
    path('create-entry/', views.CreateEntryView.as_view(), name='create-entry'),
    path('delete-entry/<str:pk>/', views.deleteEntry, name='delete'),
    path('edit-entry/<str:pk>/', views.editEntry, name='edit'),
]

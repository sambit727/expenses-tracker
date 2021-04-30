from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('entry-list/', views.entryList, name='entry-list'),
    path('create-entry/', views.CreateEntryView.as_view(), name='create-entry'),
    path('delete-entry/<str:pk>/', views.deleteEntry, name='delete'),
    path('edit-entry/<str:pk>/', views.editEntry, name='edit'),
    path('register/', views.register, name='register'),
    # path('register/', views.RegisterView.as_view(), name='register'),
    path('validate-username/', views.UsernameValidationView.as_view(), name='username-validate'),
    path('validate-email/', csrf_exempt(views.EmailValidationView.as_view()), name='email-validate'),
    path('validate-password/', views.PasswordValidationView.as_view(), name='password-validate'),

]

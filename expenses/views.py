import json
from validate_email import validate_email

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.contrib import messages

from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import EntrySerializer
from .serializers import CreateEntrySerializer

from .models import *
from .forms import *




def index(request):
    account = Account.objects.first()
    entries = EntryItem.objects.all()
    last_entry = EntryItem.objects.latest('date')
    # test = account.entryitem_set.all()
    # print(test)

    total = sum([item.amount for item in entries])

    form = EntryForm()

    # if request.method == 'POST':
    #     form = EntryForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     return redirect('/')

    if len(entries) > 0:
        # daily_avg = account.total_spending / len(entries)
        daily_avg = total / len(entries)

        spendings_track = daily_avg * 30
        savings_track = 450 - spendings_track
    else:
        daily_avg = 0
        spendings_track = 0
        savings_track = 450

    x_labels = [x.date for x in entries]

    y_labels = [y.amount for y in entries]

    context = {'entries':entries,
                'account':account,
                'form':form,
                'daily_avg':daily_avg,
                'spendings_track':spendings_track,
                'savings_track':savings_track,
                'x_labels':json.dumps(x_labels, indent=4, sort_keys=True, default=str),
                'y_labels':y_labels,}

    return render(request, 'expenses/index.html', context)


@api_view(['GET'])
def entryList(request):
    entries = EntryItem.objects.all().order_by('-id')
    serializer = EntrySerializer(entries, many=True)
    
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteEntry(request, pk):
    entry = EntryItem.objects.get(id=pk)
    entry.delete()
    return Response('Entry Successfully Deleted')


@api_view(['POST'])
def editEntry(request, pk):
	entry = EntryItem.objects.get(id=pk)
	serializer = EntrySerializer(instance=entry, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


class CreateEntryView(APIView):
    authentication_classes = (TokenAuthentication,)
    serializer_class = CreateEntrySerializer
    
    def post(self, request, format=None):    
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            category = serializer.data.get('category')
            amount = serializer.data.get('amount')
            entry = EntryItem(category=category, amount=amount)
            entry.save()
            return Response(CreateEntrySerializer(entry).data, status=status.HTTP_201_CREATED)
        
        
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)



# class RegisterView(TemplateView):
#     def get(self, request):
#         return HttpResponse(request, 'expenses/register.html', status=200)
    
#     def post(self, request):
#         return messages.success(request, 'Successfully created an account!')


def register(request):
    if request.method =='GET':
        return render(request, 'expenses/register.html')   
     
    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        context = {
            'fieldValues':request.POST
        }
        
        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password) < 6:
                    messages.error(request, 'Password too short')
                    return render(request, 'expenses/register.html', context=context) 
                
                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.save()
                messages.success(request, 'Account successfully created!')
                return render(request, 'expenses/register.html')  
        
        return render(request, 'expenses/register.html')    
        
        

class UsernameValidationView(APIView):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'username should be alphanumeric'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'username is already taken'})

        return JsonResponse({'username_valid': True})
    
    
class EmailValidationView(APIView):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error': 'Email is invalid'})
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'Email is already taken'})

        return JsonResponse({'email_valid': True})
    
    
class PasswordValidationView(APIView):
    def post(self, request):
        data = json.loads(request.body)
        password = data['password']
        
        if len(password) < 6:
            return JsonResponse({'password_error': 'Password is too short'})
        else:
            return JsonResponse({'password_valid': True})

        

        
        
    
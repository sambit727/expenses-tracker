from django.shortcuts import render, redirect
from django.http import HttpResponse
from .serializers import CreateEntrySerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response

import json

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

    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

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

def deleteEntry(request, pk):
    entry = EntryItem.objects.get(id=pk)
    entry.delete()
    context = {'entry':entry}
    return redirect('/')

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
            return Response(EntryItemSerializer(entry).data, status=status.HTTP_201_CREATED)
        
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)

from django.shortcuts import render, redirect
from django.http import HttpResponse

import json

from .models import *
from .forms import *

def index(request):

    account = Account.objects.first()
    entries = EntryItem.objects.all()

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


#['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']

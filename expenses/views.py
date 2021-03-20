from django.shortcuts import render
from django.http import HttpResponse

from .models import *
# Create your views here.

def index(request):
    entries = EntryItem.objects.all()
    account = Account.objects.all()

    total = 0
    for entry in entries:
        total += entry.amount

    daily_avg = total / len(entries)

    spendings_track = daily_avg * 30

    savings_track = 450 - spendings_track

    x_labels = [x.pk for x in entries]

    y_labels = [y.amount for y in entries]

    context = {'entries':entries,
                'total':total,
                'daily_avg':daily_avg,
                'spendings_track':spendings_track,
                'savings_track':savings_track,
                'x_labels':x_labels,
                'y_labels':y_labels,}

    return render(request, 'expenses/index.html', context)


#['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']

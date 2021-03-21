from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#
# class User(models.Model):
#     '''The authenticated user accessing their account'''
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
#     name = models.CharField(max_length=200, null=True)
#
#     def __str__(self):
#         return self.name


class Account(models.Model):
    '''The account of the user, containing several EntryItem objects'''
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)

    @property
    def total_spending(self):
        account_items = self.entryitem_set.all()
        total = sum([item.amount for item in account_items])
        return total


class EntryItem(models.Model):
    '''The entry submitted to the Account by a User'''
    date = models.DateField(auto_now_add = True)
    category = models.CharField(max_length=20, null=True)
    amount = models.FloatField()
    balance = models.FloatField()
    entry = models.ForeignKey(Account, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return (self.category + ': £' + str(self.amount))

# takes model python code and turn them into json

from rest_framework import serializers
from .models import EntryItem

class CreateEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = EntryItem
        fields = ('category', 'amount')
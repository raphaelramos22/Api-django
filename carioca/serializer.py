from .models import Times
from rest_framework import serializers


class TimesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Times
        fields = '__all__'

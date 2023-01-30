from .models import Times
from .serializer import TimesSerializer
from rest_framework import viewsets


class TimesViewSet(viewsets.ModelViewSet):
    queryset = Times.objects.all()
    serializer_class = TimesSerializer

from django.shortcuts import render
from rest_framework import viewsets,permissions,generics
from pastebin_backend.models import *
from pastebin_backend.serializers import *
# Create your views here.

class CreatePaste(generics.CreateAPIView):
    serializer_class = CreatePasteSerializer

# get paste
class GetPaste(generics.RetrieveAPIView):
    serializer_class = GetPasteSerializer
    # queryset = Paste.objects.all()
    def get_queryset(self):
        print(self.kwargs['pk'])
        queryset = Paste.objects.filter(paste_id=self.kwargs['pk']).filter(expire_time__gt=int(time.time()))
        return queryset
    # lookup_field = 'paste_id'
    
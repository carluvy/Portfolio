from django.shortcuts import render
from rest_framework.views import APIView
from swahiliApi.models import Word
from swahiliApi.serializers import WordSerializer
from rest_framework import permissions, status, generics
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView, \
    RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView


# Create your views here.


class WordListAPIView(ListAPIView):
    """This endpoint list all of the available words from the database"""
    queryset = Word.objects.all().order_by('word')

    serializer_class = WordSerializer


class CreateWordAPIView(generics.ListCreateAPIView):
    """This endpoint allows for creation of a word"""
    queryset = Word.objects.all()
    serializer_class = WordSerializer


class UpdateWordAPIView(RetrieveUpdateDestroyAPIView):
    """This endpoint allows for updating a specific word by passing in the id of the word to update"""
    queryset = Word.objects.all()
    serializer_class = WordSerializer

    def patch(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class DeleteWordAPIView(RetrieveDestroyAPIView):
    """This endpoint allows for deletion of a specific word from the database"""
    queryset = Word.objects.all().order_by('word')
    serializer_class = WordSerializer

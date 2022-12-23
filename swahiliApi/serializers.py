from rest_framework import serializers

from swahiliApi.models import Word


class WordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word
        fields = ['word', 'state', 'translation']

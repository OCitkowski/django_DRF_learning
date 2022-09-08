from rest_framework import serializers
from .models import Test, CommentTest


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('title', 'text', 'quality', 'date_update')

class CommentTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentTest
        fields = ('title', 'test')

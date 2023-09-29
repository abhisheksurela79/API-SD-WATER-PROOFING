from rest_framework import serializers
from . import models


class PDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PDF
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Videos
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Images
        fields = '__all__'

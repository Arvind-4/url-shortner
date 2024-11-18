from rest_framework import serializers
from shortner.validators import validate_url

class URLSerializer(serializers.Serializer):
    url = serializers.CharField(max_length=220, validators=[validate_url])
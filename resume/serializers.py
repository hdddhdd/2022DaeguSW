from rest_framework import serializers
from .models import Resume

class FileTestSerializer(serializers.ModelSerializer):
    path = serializers.FileField(required=False)

    class Meta:
        model = Resume
        fields = '__all__'
        read_only_fields = ('user_id', )
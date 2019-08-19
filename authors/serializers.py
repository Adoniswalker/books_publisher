from rest_framework import serializers

from authors.models import Authors


class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = "__all__"

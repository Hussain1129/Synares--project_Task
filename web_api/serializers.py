from rest_framework import serializers
from .models import StudentModel, WebUrl


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentModel
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        return StudentModel.objects.create(**validated_data)


class Urlserializer(serializers.ModelSerializer):
    class Meta:
        model = WebUrl
        fields = ["urlname"]

    # ? This is optional, we can either use this

    # def create(self, validated_data):
    #     return WebUrl.objects.create(**validated_data)

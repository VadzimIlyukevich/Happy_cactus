from rest_framework import serializers
from .models import *


class CactusProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CactusProduct
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class SucculentProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SucculentProduct
        fields = "__all__"


# class VolunteerCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Volunteer
#         fields = "__all__"
#
#
# class FormSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = FormOfCat
#         fields = "__all__"
#
#
# class FormListSerializer(serializers.ModelSerializer):
#     category_form_cat = BreedSerializer()
#
#     class Meta:
#         model = FormOfCat
#         fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "password")

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


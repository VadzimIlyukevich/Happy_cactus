from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .models import *


def check_edit_permission(request, obj):
    if request.user.is_superuser:
        return True
    else:
        return obj == request.user


class BaseApiView(APIView):
    def get(self, request):
        cactus = CactusProduct.objects.all()
        serializer = CactusProductSerializer(cactus, many=True)
        return Response(serializer.data)


class CactusProductApiViewsSet(viewsets.ModelViewSet):
    queryset = CactusProduct.objects.all()
    serializer_class = CactusProductSerializer

    action_to_serializer = {
        'list': CactusProductSerializer,
        'retrieve': CactusProductSerializer,
    }

    def get_serializer_class(self):
        return self.action_to_serializer.get(
            self.action,
            self.serializer_class
        )


class SucculentProductApiViewsSet(viewsets.ModelViewSet):
    queryset = CactusProduct.objects.all()
    serializer_class = SucculentProductSerializer

    action_to_serializer = {
        'list': SucculentProductSerializer,
        'retrieve': SucculentProductSerializer,
    }

    def get_serializer_class(self):
        return self.action_to_serializer.get(
            self.action,
            self.serializer_class
        )


class CategoryApiViewsSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    action_to_serializer = {
        'list': CategorySerializer,
        'retrieve': CategorySerializer,
    }

    def get_serializer_class(self):
        return self.action_to_serializer.get(
            self.action,
            self.serializer_class
        )


class CreateUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            new_user = serializer.save()
            if new_user:
                return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class LogoutUser(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

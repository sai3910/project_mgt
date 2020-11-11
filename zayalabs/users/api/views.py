from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin,ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated

User = get_user_model()


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)

class CreateUserViewSet(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny,]
    # queryset = User.objects.all()
    # lookup_field = "username"

    # def get_queryset(self, *args, **kwargs):
    #     return self.queryset.filter(id=self.request.user.id)

    # @action(detail=False, methods=["GET"])
    # def me(self, request):
    #     serializer = UserSerializer(request.user, context={"request": request})
    #     return Response(status=status.HTTP_200_OK, data=serializer.data)

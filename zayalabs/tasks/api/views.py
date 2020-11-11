from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin,ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.generics import CreateAPIView
from .serializers import BoardSerializer, CardSerializer, ListSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from tasks.models import Board, Card, List
from rest_framework import serializers
# User = get_user_model()


class BoardViewSet(ModelViewSet):
    serializer_class = BoardSerializer
    queryset = Board.objects.all()
    lookup_field = "title"

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(created_by=self.request.user)

    # def perform_create(self, serializer):
    #     # import ipdb;ipdb.set_trace()
    #     if self.request.user.board_user.count()>10:
    #         print("yes")
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     return Response(status=status.HTTP_200_OK, data=serializer.data)
    # def perform_create(self, serializer):
    #     import ipdb;ipdb.set_trace()
    #     serializer.save(created_by=self.request.user)
    # @action(detail=False, methods=["GET"])
    # def me(self, request):
    #     serializer = UserSerializer(request.user, context={"request": request})
    #     return Response(status=status.HTTP_200_OK, data=serializer.data)
class CardViewSet(ModelViewSet):
    serializer_class = CardSerializer
    queryset = Card.objects.all()
    lookup_field = "title"

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(created_by=self.request.user.id)
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ListViewSet(ModelViewSet):
    serializer_class = ListSerializer
    queryset = List.objects.all()
    lookup_field = "title"

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(created_by=self.request.user.id)
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
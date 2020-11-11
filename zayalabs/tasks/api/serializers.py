from django.contrib.auth import get_user_model
from rest_framework import serializers, fields
from tasks.models import Board,Card, List
from rest_framework.exceptions import ValidationError

User = get_user_model()


class BoardSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def create(self, validated_data):
        users =validated_data['users']
        usr_obj = validated_data['created_by']
        # import ipdb;ipdb.set_trace()
        if usr_obj.board_user.count()<=10:
            board_obj = Board.objects.create(

                title = validated_data['title'],
                description = validated_data['description'],
                created_by = validated_data['created_by']

                )

            board_obj.save()
            for user in users:
                board_obj.users.add(user)
            board_obj.save()
            return board_obj
        else:
            raise ValidationError("You have exceeded limit of boards(10)")

    class Meta:
        model = Board
        fields = ["title", "description", "users", "created_by"]



class CardSerializer(serializers.ModelSerializer):
    
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    modified_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    due_date = fields.DateField(input_formats=['%Y-%m-%d'])
    def create(self, validated_data):
        users =validated_data['users']
        card_obj = Card.objects.create(
            title = validated_data['title'],
            description = validated_data['description'],
            due_date = validated_data['due_date'],
            card_list = validated_data['card_list'],
            status = validated_data['status'],
            attachements = validated_data['attachements'],
            created_by = validated_data['created_by'],

            )
        card_obj.save()
        card_obj.save()
        for user in users:
            card_obj.users.add(user)
        card_obj.save()
        return card_obj

    class Meta:
        model = Card
        fields = ['title',
            'description',
            'modified_on',
            'due_date',
            'card_list',
            'status',
            'attachements',
            'created_by',
            'modified_by',
            'users']
        read_only_fields=["created_by","modified_by"]



class ListSerializer(serializers.ModelSerializer):
    
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    modified_by = serializers.HiddenField(default=serializers.CurrentUserDefault())


    
    def create(self, validated_data):
        card_obj = List.objects.create(
            board = validated_data['board'],
            created_by = validated_data['created_by'],
            modified_by = validated_data['modified_by'],

            )
        card_obj.save()
        return card_obj

    class Meta:
        model = List
        fields = ['board',
            'created_by',
            'modified_by',]
        read_only_fields=["created_by",]


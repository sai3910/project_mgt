from django.db import models

# Create your models here.
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
# from users.models import User
User = get_user_model()


class Board(TimeStampedModel):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    users = models.ManyToManyField(User)
    created_by = models.ForeignKey(User, related_name='board_user', null=True, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.title
class List(TimeStampedModel):
    """
    Lists contain cards and have an order within a board
    """
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='lists')

    # order = models.PositiveIntegerField(blank=False, null=False, default=1)

    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='list_created')
    modified_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='list_modified')

    def __str__(self):
        return '%s - %s' % (self.board, self.created_by)


class Card(TimeStampedModel):
    TO_DO = "TODO"
    IN_PROGRESS = "IP"
    DONE = "DONE"

    TASK_STATUS_CHOICES = (
        (TO_DO, 'To Do'),
        (IN_PROGRESS, 'In Progress'),
        (DONE, 'Done'),
    )

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    modified_on = models.DateTimeField(auto_now=True)
    due_date = models.DateField(auto_now=False)
    card_list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='card_list')
    
    status = models.CharField(
        max_length = 4,
        choices = TASK_STATUS_CHOICES,
    )
    # board = models.ForeignKey(Board, on_delete=models.PROTECT, null=True, blank=True)
    attachements = models.FileField(
        _('attachement File'),
        upload_to='attachements/'
    )
    created_by = models.ForeignKey(User, related_name='card_created_by', null=False, on_delete=models.PROTECT)
    modified_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='card_modified_by')

    accomplished_by = models.ForeignKey(User, related_name='accomplished_by', null=True, on_delete=models.SET_NULL)
   
    def __str__(self):
        return '%s - %s' % (self.title, self.description)



class Account(TimeStampedModel):
    """docstring for Account"""
    # ROLE_CHOICES = (
    #     ('board_admin', 'BOARD_ADMIN'),
    #     ('board_member', 'BOARD_MEMBER'),
    # )
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='us_user'
    )

    # # boards = models.ForeignKey()
    # boards = models.ManyToManyField(Board,related_name='account_boards', blank=True)
    # tasks = models.ManyToManyField(Task,related_name='account_tasks', blank=True)

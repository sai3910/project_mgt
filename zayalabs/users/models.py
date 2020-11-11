from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.conf import settings# Create your models here.
# from .managers import ModelManager

# class Membership(models.Model):
#     slug = models.SlugField(null=True, blank=True)
#     membership_type = models.CharField(
#     choices=MEMBERSHIP_CHOICES, default='Free',
#     max_length=30
#       )
#     def __str__(self):
#        return self.membership_type


 

class User(AbstractUser):
    MEMBERSHIP_CHOICES = (
    ('pre', 'Premium'),
    ('free', 'Free')
    )
    """Default user for zayalabs."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    # account_type = models.ForeignKey(Membership,related_name='account_membership',on_delete=models.PROTECT,null=True)
    account_type = models.CharField(
    choices=MEMBERSHIP_CHOICES, default='Free',
    max_length=30
      )
    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


# class Account(TimeStampedModel):
#     """docstring for Account"""
#     # ROLE_CHOICES = (
#     #     ('board_admin', 'BOARD_ADMIN'),
#     #     ('board_member', 'BOARD_MEMBER'),
#     # )
#     user = models.OneToOneField(
#         User,
#         on_delete=models.PROTECT,
#         null=True,
#         blank=True,
#         related_name='us_user'
#     )

    # boards = models.ForeignKey(Board,related_name='user_boards',on_delete=models.PROTECT)

#     email = models.EmailField(
#         _("email address"),
#         unique=True,
#         blank=False,
#         null=False,
#         max_length=254
#     )


#     full_name = models.CharField(max_length=100, blank=True)
#     account_type = models.ForeignKey(Membership,related_name='account_membership',on_delete=models.PROTECT)
#     # role = models.CharField(
#     #     max_length=2000,
#     #     choices=ROLE_CHOICES,
#     #     default='board_member'
#     # )
#     #----- For Email & Mobile---------------#


#     mobile = models.CharField(max_length=1600, blank=True)

#     # objects = ModelManager()


#     # @property
#     # def is_board_member(self):
#     #     return self.role == 'board_member'

#     # @property
#     # def is_board_admin(self):
#     #     return self.role == 'board_admin'


    # 
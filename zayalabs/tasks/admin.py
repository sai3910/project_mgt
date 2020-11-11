from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from tasks.models import Account, Board, List, Card
# from zayalabs.users.forms import UserChangeForm, UserCreationForm

# @admin.register(Account)
# @admin.register(Board)
# @admin.register(Task)

admin.site.register(Account)
admin.site.register(Board)
admin.site.register(Card)
admin.site.register(List)

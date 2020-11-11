from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from zayalabs.users.api.views import UserViewSet,CreateUserViewSet
from zayalabs.tasks.api.views import BoardViewSet, ListViewSet, CardViewSet
from django.urls import re_path, path

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("tasks/board", BoardViewSet)
router.register("tasks/list", ListViewSet)
router.register("tasks/card", CardViewSet)




app_name = "api"
urlpatterns = router.urls
# urlpatterns+=[
# 	# path("register/", CreateUserViewSet.as_view(), name="register"),
# ]

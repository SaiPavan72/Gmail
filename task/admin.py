from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

from gmail.settings import AUTH_USER_MODEL
from task.models import Gmail, Registration, MyUser

admin.site.register(Gmail)
admin.site.register(Registration)
admin.site.register(MyUser)
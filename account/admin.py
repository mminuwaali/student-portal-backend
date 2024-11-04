from . import models
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    fieldsets = [
        (_("Basic Info"), {"fields": ["email", "username", "password"]}),
        (_("Important Dates"), {"fields": ["last_login", "date_joined"]}),
        (
            _("Additonal Info"),
            {"fields": ["profile", "first_name", "last_name", "phone_number"]},
        ),
        (
            _("Permissions"),
            {
                "fields": [
                    "groups",
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "user_permissions",
                ]
            },
        ),
    ]

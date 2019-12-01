from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'gender',
        'profile_image',
    )
    fieldsets = AuthUserAdmin.fieldsets + (("유저 부가 정보", {
        "fields": (
            "profile_image", "bio", "gender",
            )
        }),)


@admin.register(models.UserLike)
class UserLikeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'userlike_to',
        'userlike_from',
    )


@admin.register(models.Letter)
class LetterAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'letter_to',
        'letter_from',
        'check',
    )



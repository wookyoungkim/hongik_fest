from django.contrib import admin
from . import models


@admin.register(models.Bar)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'text',
    )


@admin.register(models.BarLike)
class BarLikeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'bar',
        'creator',
    )
# Generated by Django 2.1.8 on 2019-05-13 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_user_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='delete',
            field=models.BooleanField(default=False),
        ),
    ]

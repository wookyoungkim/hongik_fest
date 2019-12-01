# Generated by Django 2.1.8 on 2019-05-11 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
                ('represent_image', models.ImageField(upload_to='bars/')),
                ('first_image', models.ImageField(upload_to='bars/')),
                ('second_image', models.ImageField(upload_to='bars/')),
                ('third_image', models.ImageField(upload_to='bars/')),
                ('text', models.TextField(max_length=200)),
                ('location_url', models.TextField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BarLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('bar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='bars.Bar')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

# Generated by Django 2.1.8 on 2019-05-12 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bars', '0002_barlike_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bar',
            name='first_image',
            field=models.ImageField(upload_to='bars'),
        ),
        migrations.AlterField(
            model_name='bar',
            name='represent_image',
            field=models.ImageField(upload_to='bars'),
        ),
        migrations.AlterField(
            model_name='bar',
            name='second_image',
            field=models.ImageField(upload_to='bars'),
        ),
        migrations.AlterField(
            model_name='bar',
            name='third_image',
            field=models.ImageField(upload_to='bars'),
        ),
    ]
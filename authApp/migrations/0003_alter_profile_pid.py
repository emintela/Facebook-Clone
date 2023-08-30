# Generated by Django 4.2.2 on 2023-08-30 06:10

from django.db import migrations
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pid',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvxyz123', length=7, max_length=25, prefix=''),
        ),
    ]
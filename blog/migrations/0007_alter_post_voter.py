# Generated by Django 3.2.8 on 2021-11-07 18:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_auto_20211107_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='voter',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]

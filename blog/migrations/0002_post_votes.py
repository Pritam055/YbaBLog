# Generated by Django 3.2.8 on 2021-11-07 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='votes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
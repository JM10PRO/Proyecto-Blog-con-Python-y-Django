# Generated by Django 4.1.3 on 2023-01-25 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.BigIntegerField(default=0),
        ),
    ]
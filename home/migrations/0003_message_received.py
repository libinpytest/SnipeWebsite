# Generated by Django 4.2.2 on 2023-06-18 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_message_is_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='received',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

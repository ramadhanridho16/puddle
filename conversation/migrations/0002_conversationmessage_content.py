# Generated by Django 4.2.1 on 2023-07-20 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversationmessage',
            name='content',
            field=models.TextField(default='Default content'),
        ),
    ]

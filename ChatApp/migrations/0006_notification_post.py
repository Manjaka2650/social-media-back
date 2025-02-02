# Generated by Django 5.0.6 on 2024-08-01 07:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChatApp', '0005_notification_sender'),
        ('base', '0009_delete_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_post', to='base.posts'),
        ),
    ]

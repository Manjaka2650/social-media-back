# Generated by Django 5.0.6 on 2024-08-04 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChatApp', '0013_alter_message_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pre_image',
        ),
        migrations.AddField(
            model_name='message',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='video/message_video'),
        ),
        migrations.AlterField(
            model_name='message',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/message_image/'),
        ),
    ]

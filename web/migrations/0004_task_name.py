# Generated by Django 5.1.7 on 2025-04-16 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_feedback_comment_alter_feedback_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='name',
            field=models.CharField(default='No name', max_length=255),
        ),
    ]

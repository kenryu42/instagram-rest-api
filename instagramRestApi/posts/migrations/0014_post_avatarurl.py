# Generated by Django 3.2.3 on 2021-05-18 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_alter_post_currentname'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='avatarUrl',
            field=models.CharField(default='', max_length=100),
        ),
    ]

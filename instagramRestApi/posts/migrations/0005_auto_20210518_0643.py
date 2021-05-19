# Generated by Django 3.2.3 on 2021-05-18 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20210518_0559'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='imageUri',
            new_name='imageBinary',
        ),
        migrations.AddField(
            model_name='post',
            name='dataType',
            field=models.CharField(default='', max_length=50),
        ),
    ]
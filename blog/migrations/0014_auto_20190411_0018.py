# Generated by Django 2.1.7 on 2019-04-10 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20190411_0009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='name',
            new_name='title',
        ),
    ]

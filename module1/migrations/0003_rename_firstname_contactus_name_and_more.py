# Generated by Django 5.0 on 2024-02-10 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0002_contactus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='firstname',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='lastname',
        ),
    ]

# Generated by Django 3.2.9 on 2021-11-16 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scheduleitem',
            old_name='product',
            new_name='meal',
        ),
        migrations.RenameField(
            model_name='scheduleitem',
            old_name='list',
            new_name='schedule',
        ),
    ]

# Generated by Django 3.1 on 2020-08-28 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='subjec',
            new_name='subject',
        ),
    ]

# Generated by Django 4.2.4 on 2024-02-23 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_useraccount_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='image',
        ),
    ]

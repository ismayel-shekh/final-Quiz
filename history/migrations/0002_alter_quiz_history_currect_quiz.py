# Generated by Django 4.2.4 on 2024-02-28 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz_history',
            name='currect_quiz',
            field=models.IntegerField(default=0),
        ),
    ]
# Generated by Django 4.2.4 on 2024-02-28 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_useraccount_currect_quiz'),
        ('history', '0004_alter_quiz_history_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz_history',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.useraccount'),
        ),
    ]
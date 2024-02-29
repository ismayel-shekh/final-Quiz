# Generated by Django 4.2.4 on 2024-02-28 11:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0005_alter_useraccount_currect_quiz'),
        ('history', '0005_alter_quiz_history_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz_history',
            name='user_account',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.useraccount'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quiz_history',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 4.1.1 on 2022-09-25 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='user_name',
            field=models.CharField(max_length=30, verbose_name='이름'),
        ),
    ]
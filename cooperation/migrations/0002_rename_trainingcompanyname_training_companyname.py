# Generated by Django 4.1.1 on 2022-09-24 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cooperation", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="training",
            old_name="trainingcompanyName",
            new_name="companyName",
        ),
    ]

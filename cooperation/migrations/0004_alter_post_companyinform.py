# Generated by Django 4.1.1 on 2022-09-25 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "cooperation",
            "0003_alter_companyname_name_alter_post_companyinform_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="companyInform",
            field=models.CharField(max_length=54),
        ),
    ]

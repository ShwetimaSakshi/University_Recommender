# Generated by Django 5.0.4 on 2024-04-23 03:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gradvisor", "0003_applicant_passwordval_applicant_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="applicant",
            name="researchExperience",
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 5.0.4 on 2024-04-27 21:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gradvisor", "0006_alter_applicant_gre_score"),
    ]

    operations = [
        migrations.AlterField(
            model_name="applicant",
            name="cgpa",
            field=models.FloatField(default=0),
        ),
    ]

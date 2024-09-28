# Generated by Django 4.2.16 on 2024-09-16 13:55

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0007_subnet_code_name_subnet_github_repo_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="subnet",
            old_name="code_name",
            new_name="codename",
        ),
        migrations.AlterField(
            model_name="subnet",
            name="maintainers_id",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=255), blank=True, null=True, size=None
            ),
        ),
    ]
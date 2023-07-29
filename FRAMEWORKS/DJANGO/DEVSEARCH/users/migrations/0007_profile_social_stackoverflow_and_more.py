# Generated by Django 4.2 on 2023-05-06 12:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0006_alter_skill_owner"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="social_stackoverflow",
            field=models.URLField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.URLValidator(
                        regex="https://stackoverflow.com"
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="social_github",
            field=models.URLField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.URLValidator(regex="https://github.com")
                ],
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="social_linkedin",
            field=models.URLField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.URLValidator(
                        regex="https://www.linkedin.com"
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="social_twitter",
            field=models.URLField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.URLValidator(regex="https://twitter.com")
                ],
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="social_youtube",
            field=models.URLField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.URLValidator(regex="https://youtube.com")
                ],
            ),
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-10 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartment',
            name='cite',
        ),
        migrations.RemoveField(
            model_name='room',
            name='cite',
        ),
        migrations.RemoveField(
            model_name='studio',
            name='cite',
        ),
        migrations.AddField(
            model_name='cite',
            name='apartment',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='house.apartment'),
        ),
        migrations.AddField(
            model_name='cite',
            name='room',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='house.room'),
        ),
        migrations.AddField(
            model_name='cite',
            name='studio',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='house.studio'),
        ),
    ]
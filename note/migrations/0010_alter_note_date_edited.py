# Generated by Django 3.2.7 on 2021-09-13 20:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0009_note_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='date_edited',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
# Generated by Django 3.2.7 on 2021-09-11 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='competed',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]

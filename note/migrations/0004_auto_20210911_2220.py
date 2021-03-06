# Generated by Django 3.2.7 on 2021-09-11 19:20

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_alter_note_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='competed',
        ),
        migrations.AddField(
            model_name='note',
            name='completed',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='note',
            name='body',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='date_edited',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='favorite',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='note',
            name='public',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='note',
            name='views',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]

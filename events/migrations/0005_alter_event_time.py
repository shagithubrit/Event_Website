# Generated by Django 4.2.1 on 2023-06-07 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_eventuser_event_event_createdby_delete_entry_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date_published'),
        ),
    ]

# Generated by Django 4.1.5 on 2023-12-23 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactme',
            name='created_at',
        ),
    ]
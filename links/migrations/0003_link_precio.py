# Generated by Django 3.1.3 on 2021-01-04 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_link_posted_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='precio',
            field=models.FloatField(default=0),
        ),
    ]
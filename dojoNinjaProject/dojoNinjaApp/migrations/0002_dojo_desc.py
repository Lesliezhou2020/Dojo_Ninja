# Generated by Django 3.1 on 2020-08-12 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojoNinjaApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default='old dojo'),
        ),
    ]

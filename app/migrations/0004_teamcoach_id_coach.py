# Generated by Django 4.1.4 on 2022-12-07 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_teamcoach'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamcoach',
            name='id_coach',
            field=models.IntegerField(null=True),
        ),
    ]

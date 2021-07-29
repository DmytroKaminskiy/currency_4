# Generated by Django 3.2.3 on 2021-07-29 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analytics',
            name='request_method',
            field=models.PositiveSmallIntegerField(choices=[(0, 'GET'), (1, 'POST'), (2, 'PUT'), (3, 'PATCH'), (4, 'DELETE')]),
        ),
    ]

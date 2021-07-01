# Generated by Django 3.2.3 on 2021-07-01 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0007_remove_rate_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rate',
            name='type_new',
        ),
        migrations.AddField(
            model_name='rate',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Dollar'), (1, 'Euro')], default=0),
            preserve_default=False,
        ),
    ]
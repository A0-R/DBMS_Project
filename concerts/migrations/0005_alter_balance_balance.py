# Generated by Django 4.0.4 on 2022-04-24 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concerts', '0004_alter_hall_hall_type_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='balance',
            field=models.IntegerField(default=0),
        ),
    ]

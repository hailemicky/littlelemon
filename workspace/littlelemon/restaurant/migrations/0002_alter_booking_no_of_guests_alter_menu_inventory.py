# Generated by Django 4.2 on 2023-04-20 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='no_of_guests',
            field=models.SmallIntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='inventory',
            field=models.SmallIntegerField(db_index=True),
        ),
    ]
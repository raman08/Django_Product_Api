# Generated by Django 3.2.6 on 2021-08-24 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Phone'),
        ),
    ]
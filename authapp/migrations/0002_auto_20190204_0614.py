# Generated by Django 2.1.5 on 2019-02-04 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='age',
            field=models.PositiveIntegerField(default=20, verbose_name='Age'),
        ),
    ]

# Generated by Django 2.2 on 2019-04-18 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='country',
            field=models.CharField(max_length=45, null=True, verbose_name='Country'),
        ),
    ]

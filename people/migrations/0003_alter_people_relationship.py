# Generated by Django 3.2.5 on 2021-09-01 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20210824_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='relationship',
            field=models.CharField(choices=[('Immediate', 'Immediate'), ('Distant', 'Distant'), ('Friend', 'Friend')], max_length=50),
        ),
    ]

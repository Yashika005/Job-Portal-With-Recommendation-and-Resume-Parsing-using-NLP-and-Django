# Generated by Django 4.1.7 on 2023-04-19 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentuser',
            name='type',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
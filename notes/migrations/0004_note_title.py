# Generated by Django 3.1.5 on 2021-02-01 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20210201_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=60, null=True),
        ),
    ]

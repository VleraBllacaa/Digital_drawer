# Generated by Django 3.2 on 2021-04-27 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digitalfile', '0004_auto_20210428_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='digitalfiles',
            name='FileUpload',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]

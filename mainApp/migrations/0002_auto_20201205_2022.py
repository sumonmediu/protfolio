# Generated by Django 3.0.8 on 2020-12-05 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='protfolio',
            name='project_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='protfolio',
            name='project_image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]

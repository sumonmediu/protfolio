# Generated by Django 3.0.8 on 2020-12-15 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_filesadmin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('message', models.CharField(max_length=100)),
                ('comment_from_admin', models.TextField(blank=True)),
                ('action', models.CharField(choices=[('unseen', 'UnSeen'), ('seen', 'Seen'), ('done', 'Done'), ('in Progress', 'In Progress')], default='unseen', max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='FilesAdmin',
        ),
    ]
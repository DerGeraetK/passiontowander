# Generated by Django 4.2.2 on 2023-06-25 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagecontentblock',
            name='country',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='imagecontentblock',
            name='region',
            field=models.CharField(default='', max_length=200),
        ),
    ]

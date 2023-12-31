# Generated by Django 4.2.2 on 2023-07-14 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_uploadedvideo_uploadedimage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uploadedimage',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='uploadedvideo',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='uploadedimage',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='uploadedimage',
            name='post',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='blog.post'),
        ),
        migrations.AddField(
            model_name='uploadedvideo',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='uploadedvideo',
            name='post',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='blog.post'),
        ),
        migrations.AlterField(
            model_name='headingcontentblock',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='headingcontentblock',
            name='post',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='blog.post'),
        ),
        migrations.AlterField(
            model_name='imagecontentblock',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='imagecontentblock',
            name='post',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='blog.post'),
        ),
        migrations.AlterField(
            model_name='textcontentblock',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='textcontentblock',
            name='post',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='blog.post'),
        ),
        migrations.AlterField(
            model_name='videocontentblock',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='videocontentblock',
            name='post',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='blog.post'),
        ),
    ]

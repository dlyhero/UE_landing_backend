# Generated by Django 5.0.6 on 2024-05-26 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_inquiry_alter_blogpost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.URLField(default='https://picsum.photos/77/53'),
        ),
    ]

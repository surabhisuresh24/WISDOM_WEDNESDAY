# Generated by Django 5.0.6 on 2024-08-07 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wwq', '0002_blog_image_blog_week'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='week',
            field=models.IntegerField(default=1),
        ),
    ]

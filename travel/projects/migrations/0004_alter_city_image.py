# Generated by Django 3.2.2 on 2021-06-01 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_city_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='image',
            field=models.FilePathField(path='img/'),
        ),
    ]

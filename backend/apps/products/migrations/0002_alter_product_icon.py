# Generated by Django 4.1.1 on 2022-10-17 14:50

import common.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to=common.utils.UUIDFilenameGenerator(basepath='products'), verbose_name='icon'),
        ),
    ]
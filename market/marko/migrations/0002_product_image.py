# Generated by Django 4.1.6 on 2023-02-15 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marko', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

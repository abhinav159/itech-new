# Generated by Django 4.2.1 on 2023-06-11 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_alter_cards_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]

# Generated by Django 3.2.10 on 2022-05-25 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_editor_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default='default.jpg', upload_to='articles/'),
        ),
    ]

# Generated by Django 3.2.2 on 2021-05-25 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_alter_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='static/images/', upload_to='static/images/'),
        ),
    ]

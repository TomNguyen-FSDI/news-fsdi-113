# Generated by Django 3.2.2 on 2021-05-25 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_alter_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='static/images/', upload_to='staticfiles/images/'),
        ),
    ]
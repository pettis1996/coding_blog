# Generated by Django 4.2.2 on 2023-07-16 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_blog', '0013_alter_post_img_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img_url',
            field=models.CharField(default='./main_blog/static/images/post-default-image.jpg', max_length=255),
        ),
    ]

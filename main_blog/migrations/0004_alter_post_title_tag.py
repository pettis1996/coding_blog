# Generated by Django 4.2.2 on 2023-07-05 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_blog', '0003_alter_post_title_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='{{post.title}}', max_length=255),
        ),
    ]
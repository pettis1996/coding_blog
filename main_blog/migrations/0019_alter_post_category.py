# Generated by Django 4.2.2 on 2023-07-22 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_blog', '0018_alter_post_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='general', max_length=255),
        ),
    ]

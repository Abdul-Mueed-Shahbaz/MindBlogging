# Generated by Django 4.1.4 on 2023-10-08 12:31

import ckeditor.fields
from django.db import migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='content',
            field=ckeditor.fields.RichTextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
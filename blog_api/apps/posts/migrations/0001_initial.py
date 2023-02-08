# Generated by Django 4.1.4 on 2022-12-27 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isActive', models.BooleanField(default=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField(blank=True, default='')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Blog', to='blog.blog')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]

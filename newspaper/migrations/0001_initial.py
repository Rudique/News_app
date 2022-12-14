# Generated by Django 4.1 on 2022-10-06 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('content', models.CharField(max_length=1500, verbose_name='content')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='date_of_creation')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='date_of_editing')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
            ],
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('comment', models.CharField(max_length=1500, verbose_name='comment')),
                ('article_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='newspaper.newsmodel')),
            ],
        ),
    ]

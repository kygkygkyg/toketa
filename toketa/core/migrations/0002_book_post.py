# Generated by Django 3.2.12 on 2022-04-03 09:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date_of_issue', models.TimeField()),
                ('auther', models.CharField(max_length=200)),
                ('created_at', models.TimeField(help_text='created time (this data)')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_info', models.CharField(max_length=300)),
                ('path_docs', models.CharField(max_length=300, unique=True)),
                ('created_at', models.TimeField(help_text='created time (this data)')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.book')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

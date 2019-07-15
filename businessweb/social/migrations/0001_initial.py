# Generated by Django 2.2.2 on 2019-07-15 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.SlugField(max_length=100, unique=True, verbose_name='Key Name')),
                ('name', models.CharField(max_length=200, verbose_name='Social Network')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Link')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'link',
                'verbose_name_plural': 'links',
                'ordering': ['name'],
            },
        ),
    ]
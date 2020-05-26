# Generated by Django 2.1.7 on 2020-05-23 18:08

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
                ('key', models.SlugField(max_length=100, unique=True, verbose_name='Key name')),
                ('name', models.CharField(max_length=200, verbose_name='Social network')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Link')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
            ],
            options={
                'verbose_name': 'linkcategory',
                'ordering': ['name'],
            },
        ),
    ]
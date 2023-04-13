# Generated by Django 4.2 on 2023-04-13 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('author', models.CharField(max_length=255)),
                ('publisher', models.CharField(max_length=255)),
                ('edition', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('quantity', models.IntegerField()),
                ('year', models.IntegerField()),
                ('num_pages', models.IntegerField()),
                ('language', models.CharField(max_length=50)),
                ('cover', models.ImageField(blank=True, upload_to='media/')),
            ],
        ),
    ]

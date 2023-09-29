# Generated by Django 4.2.3 on 2023-08-02 11:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_file', models.CharField(choices=[('image', 'Image'), ('video', 'Video'), ('pdf', 'PDF')], default='image', max_length=5)),
                ('name_heading', models.CharField(max_length=100)),
                ('name_caption', models.TextField()),
                ('url', models.URLField(validators=[django.core.validators.URLValidator()])),
                ('thumbnail', models.ImageField(upload_to='thumbnails/')),
                ('thumbnail_small', models.ImageField(blank=True, null=True, upload_to='thumbnails/')),
            ],
        ),
    ]

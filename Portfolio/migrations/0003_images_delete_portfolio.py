# Generated by Django 4.2.3 on 2023-08-02 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0002_portfolio_delete_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=50)),
                ('caption', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='media/photos/image')),
                ('thumbnail', models.ImageField(upload_to='media/photos/thumbnails/')),
                ('thumbnail_small', models.ImageField(blank=True, null=True, upload_to='media/photos/small thumbnails/')),
            ],
        ),
        migrations.DeleteModel(
            name='Portfolio',
        ),
    ]

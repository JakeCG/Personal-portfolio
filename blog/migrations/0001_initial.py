# Generated by Django 4.1.2 on 2022-10-13 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('pub_date', models.DateTimeField()),
                ('body', models.TextField()),
                ('images', models.ImageField(upload_to='images/')),
            ],
        ),
    ]

# Generated by Django 4.1.4 on 2023-01-06 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('address', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='PostModel',
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-06 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Co_code', models.CharField(max_length=200)),
                ('Co_name', models.CharField(max_length=200)),
                ('IBR_name', models.CharField(max_length=20)),
                ('Face_value', models.IntegerField()),
                ('DATE_OF_INCO', models.CharField(max_length=200)),
                ('CNVTOPUBDT', models.CharField(max_length=200)),
            ],
        ),
    ]

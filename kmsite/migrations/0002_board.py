# Generated by Django 2.1 on 2018-08-08 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kmsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='board',
            fields=[
                ('num', models.IntegerField(primary_key=True, serialize=False)),
                ('id', models.CharField(max_length=25)),
                ('subject', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=20000)),
                ('writedate', models.DateField(blank=True, null=True)),
                ('hits', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
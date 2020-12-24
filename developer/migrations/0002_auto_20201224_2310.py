# Generated by Django 2.2.8 on 2020-12-24 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='account',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='developer',
            name='avatar',
            field=models.ImageField(default='avatar/defaultAv.png', upload_to='avatar/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='developer',
            name='introduction',
            field=models.CharField(default='创造ing', max_length=300),
        ),
    ]

# Generated by Django 3.0.7 on 2020-06-23 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghostpost', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='poast_type',
        ),
        migrations.AddField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('r', 'Roast'), ('b', 'Boast')], default='b', max_length=10),
        ),
    ]

# Generated by Django 2.0.7 on 2019-04-18 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soccer', '0002_predictions'),
    ]

    operations = [
        migrations.AddField(
            model_name='playersinfo',
            name='picture',
            field=models.ImageField(default='DEFAULT VALUE', upload_to='images/'),
        ),
    ]

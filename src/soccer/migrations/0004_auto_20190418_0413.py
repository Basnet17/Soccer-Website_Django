# Generated by Django 2.0.7 on 2019-04-18 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soccer', '0003_playersinfo_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playersinfo',
            name='picture',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='images/'),
        ),
    ]

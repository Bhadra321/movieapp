# Generated by Django 5.0 on 2023-12-16 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movieinfo',
            name='img',
            field=models.ImageField(default='ddffdfs', upload_to='gallary'),
            preserve_default=False,
        ),
    ]
# Generated by Django 3.2.9 on 2021-12-31 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='media/user.png', null=True, upload_to='users/'),
        ),
    ]

# Generated by Django 3.2.9 on 2021-12-29 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='https://www.kbl.co.uk/wp-content/uploads/2017/11/Default-Profile-Male.jpg', null=True, upload_to='users/'),
        ),
    ]
# Generated by Django 3.0.7 on 2020-06-19 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20200619_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]
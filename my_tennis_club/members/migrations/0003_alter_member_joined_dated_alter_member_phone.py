# Generated by Django 5.0.7 on 2024-07-14 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_joined_dated_member_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='joined_dated',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]

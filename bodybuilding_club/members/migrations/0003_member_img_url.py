# Generated by Django 4.2.2 on 2023-06-21 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='img_url',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
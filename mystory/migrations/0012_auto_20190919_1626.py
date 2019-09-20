# Generated by Django 2.2.5 on 2019-09-19 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystory', '0011_story_feeling'),
    ]

    operations = [
        migrations.AddField(
            model_name='wedding_invitation',
            name='gmap',
            field=models.CharField(blank=True, max_length=500, verbose_name='Google map'),
        ),
        migrations.AlterField(
            model_name='wedding_invitation',
            name='location',
            field=models.CharField(blank=True, max_length=500, verbose_name='Địa điểm tổ chức'),
        ),
    ]
# Generated by Django 4.0.1 on 2022-03-22 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_placementbid_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='placementbid',
            options={'ordering': ['placementbid_modified']},
        ),
    ]

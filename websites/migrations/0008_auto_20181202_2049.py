# Generated by Django 2.0.5 on 2018-12-02 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0007_auto_20181202_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='u_contact',
        ),
        migrations.RemoveField(
            model_name='user',
            name='u_name',
        ),
    ]

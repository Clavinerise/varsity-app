# Generated by Django 2.0.5 on 2018-12-02 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0005_auto_20181116_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='varsity',
            name='v_file',
            field=models.FileField(blank=True, null=True, upload_to='files/%v_num'),
        ),
    ]

# Generated by Django 2.2 on 2019-03-14 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project2App', '0003_auto_20190313_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relatedcontentmodel',
            name='image',
            field=models.ImageField(default='', upload_to='site_media/'),
        ),
        migrations.AlterField(
            model_name='wikimodel',
            name='image',
            field=models.ImageField(null=True, upload_to='site_media'),
        ),
    ]

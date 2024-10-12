# Generated by Django 4.2.16 on 2024-10-02 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0007_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='nightLogo',
            field=models.FileField(default=None, upload_to='images/skill/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='skill',
            name='logo',
            field=models.FileField(upload_to='images/skill/'),
        ),
    ]
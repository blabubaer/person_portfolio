# Generated by Django 3.1.6 on 2021-02-04 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_job_git_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='title',
            field=models.CharField(default='Test', max_length=255),
        ),
        migrations.AlterField(
            model_name='job',
            name='git_page',
            field=models.URLField(),
        ),
    ]

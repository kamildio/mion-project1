# Generated by Django 3.1 on 2023-03-13 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mionApp', '0003_auto_20230312_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='isRecommended',
            field=models.BooleanField(default=False, verbose_name='Is recommended'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='isTopTen',
            field=models.BooleanField(default=False, verbose_name='Is top ten'),
        ),
    ]

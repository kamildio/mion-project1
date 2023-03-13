

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mionApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='isRecommended',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Is top ten'),
        ),
        migrations.AddField(
            model_name='movie',
            name='isTopTen',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Is top ten'),
        ),
    ]

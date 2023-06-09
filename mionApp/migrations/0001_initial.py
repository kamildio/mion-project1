

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genreName', models.CharField(max_length=255, verbose_name='Genre name')),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieName', models.CharField(max_length=255, verbose_name='Movie name')),
                ('producer', models.CharField(max_length=255, verbose_name='Producer')),
                ('cover', models.CharField(max_length=500, verbose_name='Link to cover')),
                ('poster', models.CharField(max_length=500, verbose_name='Link to poster')),
                ('year', models.IntegerField(verbose_name='Year')),
                ('rating', models.FloatField(verbose_name='Rating')),
                ('movieLink', models.CharField(max_length=500, verbose_name='Youtube movie link')),
                ('description', models.TextField(verbose_name='Description')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mionApp.genre', verbose_name='Genre')),
            ],
        ),
    ]

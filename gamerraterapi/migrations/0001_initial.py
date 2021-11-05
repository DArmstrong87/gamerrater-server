# Generated by Django 3.2.9 on 2021-11-01 18:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('designer', models.CharField(max_length=50)),
                ('year_released', models.IntegerField()),
                ('num_players', models.IntegerField()),
                ('time_to_play', models.IntegerField()),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamerraterapi.game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamerraterapi.player')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamerraterapi.game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamerraterapi.player')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=50)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamerraterapi.game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamerraterapi.player')),
            ],
        ),
        migrations.CreateModel(
            name='GameCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamerraterapi.category')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamerraterapi.game')),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry', models.TextField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamerraterapi.game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamerraterapi.player')),
            ],
        ),
    ]
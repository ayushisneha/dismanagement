# Generated by Django 2.1.2 on 2018-10-25 15:03

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
            name='Alert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_name', models.CharField(blank=True, choices=[('Forest_Fire', 'Forest_Fire'), ('Flood', 'Flood'), ('tora', 'tora')], max_length=130, null=True)),
                ('unsafe_peoples', models.BigIntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(blank=True, choices=[('Chennnai', 'Chennnai'), ('Delhi', 'Delhi'), ('Bombay', 'Bombay'), ('Tirupati', 'Tirupati'), ('Agra', 'Agra')], max_length=130, null=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_site', models.URLField(blank=True)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('city', models.CharField(blank=True, choices=[('Chennnai', 'Chennnai'), ('Delhi', 'Delhi'), ('Bombay', 'Bombay'), ('Tirupati', 'Tirupati'), ('Agra', 'Agra')], max_length=130, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='alert',
            name='city_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.City'),
        ),
    ]

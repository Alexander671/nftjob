# Generated by Django 3.2 on 2022-04-04 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tokens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_hash', models.CharField(max_length=20, unique=True)),
                ('tx_hash', models.CharField(max_length=30, unique=True)),
                ('media_url', models.URLField()),
                ('owner', models.TextField()),
            ],
            options={
                'verbose_name': 'Token',
                'verbose_name_plural': 'Tokens',
            },
        ),
    ]
# Generated by Django 5.0.1 on 2024-02-04 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='genre',
            field=models.CharField(choices=[('adventure', 'Adventure'), ('strategy', 'Strategy'), ('role_playing', 'Role Playing'), ('puzzle', 'Puzzle'), ('card', 'Card'), ('word', 'Word'), ('not_selected', 'Not selected')], default='not_selected', max_length=20),
        ),
    ]

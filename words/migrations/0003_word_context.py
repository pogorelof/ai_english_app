# Generated by Django 5.1.2 on 2024-10-18 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0002_alter_word_guessed_alter_word_wrong'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='context',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

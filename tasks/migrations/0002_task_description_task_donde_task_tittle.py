# Generated by Django 5.0.4 on 2024-04-12 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='task',
            name='donde',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='tittle',
            field=models.CharField(default='tittle', max_length=200),
            preserve_default=False,
        ),
    ]

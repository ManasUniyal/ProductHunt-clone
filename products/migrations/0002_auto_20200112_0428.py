# Generated by Django 3.0.1 on 2020-01-11 22:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='hunter',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='url',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='votes_total',
            field=models.BigIntegerField(default=0),
        ),
    ]

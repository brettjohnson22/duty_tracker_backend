# Generated by Django 3.2.8 on 2021-12-22 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ships', '0001_initial'),
        ('authentication', '0002_auto_20211222_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ship',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ships.ship'),
        ),
    ]

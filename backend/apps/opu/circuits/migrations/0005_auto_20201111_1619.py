# Generated by Django 2.2.4 on 2020-11-11 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0006_auto_20201111_1159'),
        ('circuits', '0004_auto_20201111_1614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalcircuit',
            name='id_object',
        ),
        migrations.RemoveField(
            model_name='circuit',
            name='id_object',
        ),
        migrations.AddField(
            model_name='circuit',
            name='id_object',
            field=models.ManyToManyField(blank=True, null=True, related_name='circ_obj', to='objects.Object'),
        ),
    ]

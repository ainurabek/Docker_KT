# Generated by Django 2.2.4 on 2020-10-29 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0003_auto_20201029_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formanalysis',
            name='outfit',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='objects.Outfit', verbose_name='Предприятия'),
        ),
        migrations.AlterField(
            model_name='punkt5',
            name='outfit',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='objects.Outfit', verbose_name='Предприятия'),
        ),
        migrations.AlterField(
            model_name='punkt7',
            name='outfit',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='objects.Outfit', verbose_name='Предприятия'),
        ),
    ]

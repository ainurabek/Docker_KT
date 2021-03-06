# Generated by Django 2.2.4 on 2020-10-23 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formanalysis',
            name='punkt5',
        ),
        migrations.RemoveField(
            model_name='formanalysis',
            name='punkt7',
        ),
        migrations.AddField(
            model_name='punkt5',
            name='form_analysis',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='punkt5', to='analysis.FormAnalysis', verbose_name='Форма анализа'),
        ),
        migrations.AddField(
            model_name='punkt7',
            name='form_analysis',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='punkt7', to='analysis.FormAnalysis', verbose_name='Форма анализа'),
        ),
        migrations.AlterField(
            model_name='formanalysis',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название'),
        ),
    ]

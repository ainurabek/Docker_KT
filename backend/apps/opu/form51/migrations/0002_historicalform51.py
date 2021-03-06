# Generated by Django 2.2.4 on 2020-11-03 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_historicalcustomer'),
        ('accounts', '0001_initial'),
        ('objects', '0003_historicalip_historicalobject_historicalorder_historicaloutfit_historicalpoint'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('form51', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalForm51',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('num_ouss', models.CharField(blank=True, max_length=250, null=True, verbose_name='Номер распоряжения ОУСС')),
                ('reserve', models.CharField(blank=True, max_length=15, null=True, verbose_name='Резерва потока')),
                ('report_num', models.CharField(blank=True, max_length=200, null=True, verbose_name='Номер донесения')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('created_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='accounts.Profile')),
                ('customer', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='customer.Customer', verbose_name='Примечание (№ID, МН, Аренда)')),
                ('history_relation', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='history_form51_log', to='form51.Form51')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('object', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='objects.Object', verbose_name='КО')),
            ],
            options={
                'verbose_name': 'historical Форма 5.1',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]

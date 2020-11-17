# Generated by Django 2.2.4 on 2020-10-19 18:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        ('circuits', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
        ('objects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Примечание',
                'verbose_name_plural': 'Примечание',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateTimeField(blank=True, null=True, verbose_name='От')),
                ('date_to', models.DateTimeField(blank=True, null=True, verbose_name='До')),
                ('date_calls', models.DateTimeField(blank=True, null=True, verbose_name='Время звонка')),
                ('created_at', models.DateField(blank=True, null=True, verbose_name='Дата создания')),
                ('comments1', models.CharField(blank=True, max_length=500, null=True, verbose_name='Примечание1')),
                ('name', models.CharField(blank=True, max_length=500, null=True, verbose_name='Название')),
                ('callsorevent', models.BooleanField(default=True)),
                ('period_of_time', models.CharField(blank=True, max_length=20, null=True)),
                ('circuit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_cir', to='circuits.Circuit', verbose_name='Каналы')),
                ('contact_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='objects.OutfitWorker', verbose_name='Передал (ФИО)')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Profile', verbose_name='ФИО диспетчера')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.Customer', verbose_name='Арендаторы')),
                ('id_parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_id_parent', to='dispatching.Event')),
            ],
            options={
                'verbose_name': 'Журнал событий',
                'verbose_name_plural': 'Журнал событий',
                'ordering': ('id',),
                'get_latest_by': 'id',
            },
        ),
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.CharField(max_length=255, verbose_name='Индекс')),
                ('name', models.CharField(max_length=255, verbose_name='Название индекса')),
            ],
            options={
                'verbose_name': 'Индекс события',
                'verbose_name_plural': 'Индекс события',
            },
        ),
        migrations.CreateModel(
            name='Reason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Причины',
                'verbose_name_plural': 'Причины',
            },
        ),
        migrations.CreateModel(
            name='TypeOfJournal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Виды журнала',
                'verbose_name_plural': 'Вид журнала',
            },
        ),
        migrations.CreateModel(
            name='HistoricalEvent',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('date_from', models.DateTimeField(blank=True, null=True, verbose_name='От')),
                ('date_to', models.DateTimeField(blank=True, null=True, verbose_name='До')),
                ('date_calls', models.DateTimeField(blank=True, null=True, verbose_name='Время звонка')),
                ('created_at', models.DateField(blank=True, null=True, verbose_name='Дата создания')),
                ('comments1', models.CharField(blank=True, max_length=500, null=True, verbose_name='Примечание1')),
                ('name', models.CharField(blank=True, max_length=500, null=True, verbose_name='Название')),
                ('callsorevent', models.BooleanField(default=True)),
                ('period_of_time', models.CharField(blank=True, max_length=20, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('circuit', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='circuits.Circuit', verbose_name='Каналы')),
                ('contact_name', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='objects.OutfitWorker', verbose_name='Передал (ФИО)')),
                ('created_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='accounts.Profile', verbose_name='ФИО диспетчера')),
                ('customer', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='customer.Customer', verbose_name='Арендаторы')),
                ('history_relation', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='history_log', to='dispatching.Event')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('id_parent', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='dispatching.Event')),
                ('index1', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='dispatching.Index', verbose_name='Индекс1')),
                ('ips', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='objects.IP', verbose_name='ИПы')),
                ('object', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='objects.Object', verbose_name='КО')),
                ('point1', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='objects.Point', verbose_name='Ип от')),
                ('point2', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='objects.Point', verbose_name='Ип до')),
                ('previous', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='dispatching.Event')),
                ('reason', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='dispatching.Reason', verbose_name='Причины')),
                ('responsible_outfit', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='objects.Outfit', verbose_name='Ответственный')),
                ('send_from', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='objects.Outfit', verbose_name='Передал (предприятие)')),
                ('type_journal', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='dispatching.TypeOfJournal', verbose_name='Вид журнала')),
            ],
            options={
                'verbose_name': 'historical Журнал событий',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.AddField(
            model_name='event',
            name='index1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_index1', to='dispatching.Index', verbose_name='Индекс1'),
        ),
        migrations.AddField(
            model_name='event',
            name='ips',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_ips', to='objects.IP', verbose_name='ИПы'),
        ),
        migrations.AddField(
            model_name='event',
            name='object',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_obj', to='objects.Object', verbose_name='КО'),
        ),
        migrations.AddField(
            model_name='event',
            name='point1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='point1_event', to='objects.Point', verbose_name='Ип от'),
        ),
        migrations.AddField(
            model_name='event',
            name='point2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='point2_event', to='objects.Point', verbose_name='Ип до'),
        ),
        migrations.AddField(
            model_name='event',
            name='previous',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event_previous', to='dispatching.Event'),
        ),
        migrations.AddField(
            model_name='event',
            name='reason',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dispatching.Reason', verbose_name='Причины'),
        ),
        migrations.AddField(
            model_name='event',
            name='responsible_outfit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dispatch_outfit', to='objects.Outfit', verbose_name='Ответственный'),
        ),
        migrations.AddField(
            model_name='event',
            name='send_from',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dispatch_send_outfit', to='objects.Outfit', verbose_name='Передал (предприятие)'),
        ),
        migrations.AddField(
            model_name='event',
            name='type_journal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dispatching.TypeOfJournal', verbose_name='Вид журнала'),
        ),
    ]
# Generated by Django 2.2.1 on 2019-05-23 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'currency',
            },
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('rate', models.DecimalField(decimal_places=8, max_digits=20)),
                ('volume', models.DecimalField(decimal_places=8, max_digits=20)),
                ('currency_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='currencyapp.Currency')),
            ],
            options={
                'db_table': 'rate',
            },
        ),
    ]

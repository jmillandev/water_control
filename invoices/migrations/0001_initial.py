# Generated by Django 2.2.3 on 2020-04-07 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('houses', '0001_initial'),
        ('family_bosses', '0001_initial'),
        ('consumption_histories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paid', models.BooleanField(default=False)),
                ('payment_date', models.DateTimeField(default=None, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='family_bosses.FamilyBoss')),
                ('detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consumption_histories.ConsumptionHistory')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houses.House')),
            ],
        ),
    ]
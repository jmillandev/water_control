# Generated by Django 2.2.3 on 2020-04-06 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Measurer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measure', models.PositiveIntegerField()),
                ('last_visit', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

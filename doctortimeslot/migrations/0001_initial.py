# Generated by Django 4.2.4 on 2023-08-11 03:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorTimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starttime', models.TimeField()),
                ('endtime', models.TimeField()),
                ('day', models.IntegerField(choices=[(1, 'monday'), (2, 'tuesday'), (3, 'wednesday'), (4, 'thursday'), (5, 'friday'), (6, 'saturday')], default=1)),
                ('doctor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

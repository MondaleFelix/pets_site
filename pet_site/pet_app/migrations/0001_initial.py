# Generated by Django 3.0.5 on 2020-05-16 05:54

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
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_name', models.CharField(help_text='Pet Name', max_length=100)),
                ('species', models.CharField(help_text='Species', max_length=50)),
                ('breed', models.CharField(help_text='Breed', max_length=50)),
                ('weight_in_pounds', models.IntegerField()),
                ('owner', models.ForeignKey(help_text='Pet Owner', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_appointment', models.DateField()),
                ('duration_minutes', models.IntegerField()),
                ('special_instructions', models.TextField()),
                ('pet', models.ForeignKey(help_text='Pet that the appointment is for.', on_delete=django.db.models.deletion.CASCADE, to='pet_app.Pet')),
            ],
        ),
    ]

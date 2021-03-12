# Generated by Django 3.1.7 on 2021-03-12 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstoneapi', '0004_calendartext'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
                ('tutors', models.ManyToManyField(related_name='subjects', related_query_name='subject', to='capstoneapi.JourneyUser')),
            ],
        ),
    ]

# Generated by Django 3.2.2 on 2021-06-04 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('dob', models.DateField()),
                ('healthissue', models.CharField(default='no', max_length=30)),
                ('interest', models.CharField(default='no', max_length=30)),
                ('hobby', models.CharField(default='no', max_length=30)),
                ('phone', models.CharField(default='no', max_length=13)),
                ('economic_pref', models.CharField(default='moderate', max_length=30)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.registeration')),
            ],
        ),
    ]

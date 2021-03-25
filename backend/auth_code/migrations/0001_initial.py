# Generated by Django 3.1 on 2021-03-25 09:47

import auth_code.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=auth_code.models.code_generator, max_length=6)),
                ('userprofile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='auth_code', to='userprofile.userprofile')),
            ],
        ),
    ]

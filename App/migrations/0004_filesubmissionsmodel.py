# Generated by Django 2.2.4 on 2019-09-04 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20190824_1905'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileSubmissionsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.BooleanField(default=True)),
            ],
        ),
    ]
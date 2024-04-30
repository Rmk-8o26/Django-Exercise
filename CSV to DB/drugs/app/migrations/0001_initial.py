# Generated by Django 5.0.2 on 2024-03-01 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RepM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField()),
                ('drug_name', models.CharField(max_length=20)),
                ('drug_strength', models.CharField(max_length=20)),
                ('drug_type', models.CharField(max_length=10)),
                ('bill_date', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
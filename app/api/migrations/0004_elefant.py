# Generated by Django 4.2.4 on 2023-09-02 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_dog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Elefant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
            ],
        ),
    ]

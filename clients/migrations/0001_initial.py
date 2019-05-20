# Generated by Django 2.2.1 on 2019-05-17 18:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('properties', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=255)),
                ('mname', models.CharField(blank=True, max_length=255)),
                ('lname', models.CharField(blank=True, max_length=255)),
                ('image', models.CharField(blank=True, max_length=999)),
                ('SSN', models.CharField(blank=True, max_length=10)),
                ('streetName', models.CharField(blank=True, max_length=999)),
                ('houseNumber', models.CharField(blank=True, max_length=255)),
                ('zipCode', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(blank=True, max_length=255)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RecentlyViewed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.Properties')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.Profile')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-22 07:29
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0004_homepage_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClubRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_type', models.CharField(choices=[('OSS', 'Open Source'), ('WEB', 'Web Literacy'), ('WNC', 'Women & Children')], default='OSS', max_length=40)),
                ('club_status', models.CharField(choices=[('new', 'New Club'), ('existing', 'Existing Club'), ('notsure', 'Not Sure')], default='new', max_length=40)),
                ('club_name', models.CharField(max_length=40)),
                ('club_description', mezzanine.core.fields.RichTextField()),
                ('club_location', models.CharField(max_length=255)),
                ('club_place', models.CharField(max_length=255)),
                ('club_privacy', models.CharField(choices=[('public', 'Public Visibility'), ('open', 'Anyone Can Join'), ('private', 'Private & Closed')], default='public', max_length=40)),
                ('fullname', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('occupation', models.CharField(blank=True, max_length=255)),
                ('github_username', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]

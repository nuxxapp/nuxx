# Generated by Django 3.0.4 on 2020-06-25 14:19

from django.conf import settings
import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0007_project_anonymous'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('uuid', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('keywords', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=150), size=None)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text='recipe json')),
                ('user', models.ForeignKey(blank=True, help_text='user', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_recipes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Recipe',
                'verbose_name_plural': 'Recipes',
                'ordering': ['-id'],
            },
        ),
    ]

# Generated by Django 5.1.5 on 2025-01-22 05:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='care.basemodel')),
                ('lmp', models.DateField(blank=True, null=True)),
                ('expected_due_date', models.DateField(blank=True, null=True)),
                ('current_trimester', models.CharField(choices=[('First', 'First Trimester'), ('Second', 'Second Trimester'), ('Third', 'Third Trimester')], default='First', max_length=20)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('mother', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('care.basemodel',),
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-01 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_physician_rename_code_procedure_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='physician',
            name='password',
            field=models.CharField(default='abhi', max_length=100),
        ),
    ]
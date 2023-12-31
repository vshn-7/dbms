# Generated by Django 4.1.7 on 2023-03-01 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='physician',
            fields=[
                ('employeeid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'physician',
            },
        ),
        migrations.RenameField(
            model_name='procedure',
            old_name='Code',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='procedure',
            old_name='Cost',
            new_name='cost',
        ),
        migrations.RenameField(
            model_name='procedure',
            old_name='Name',
            new_name='name',
        ),
        migrations.CreateModel(
            name='patient',
            fields=[
                ('ssn', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('age', models.DecimalField(decimal_places=0, max_digits=4)),
                ('pcp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.physician')),
            ],
            options={
                'db_table': 'patient',
            },
        ),
    ]

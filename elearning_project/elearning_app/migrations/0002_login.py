# Generated by Django 4.2.7 on 2023-11-30 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=150)),
                ('role', models.CharField(choices=[('STD', 'Student'), ('TUT', 'Tutor'), ('ADM', 'Admin')], default='STD', max_length=4)),
            ],
            options={
                'unique_together': {('email', 'password')},
            },
        ),
    ]

# Generated by Django 3.0.4 on 2020-03-19 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='name',
            new_name='description',
        ),
        migrations.AddField(
            model_name='customuser',
            name='skill',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

# Generated by Django 4.1.3 on 2023-06-27 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0007_alter_form_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
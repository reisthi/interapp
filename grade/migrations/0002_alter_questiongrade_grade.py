# Generated by Django 3.2.8 on 2021-10-20 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grade', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questiongrade',
            name='grade',
            field=models.CharField(choices=[('N', 'Not answered'), ('P', 'Poor'), ('O', 'Okay'), ('M', 'Medium'), ('G', 'Good')], default=0, max_length=1),
        ),
    ]

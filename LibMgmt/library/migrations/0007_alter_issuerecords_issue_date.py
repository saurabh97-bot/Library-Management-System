# Generated by Django 3.2.9 on 2021-12-02 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20211202_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuerecords',
            name='issue_date',
            field=models.DateField(),
        ),
    ]

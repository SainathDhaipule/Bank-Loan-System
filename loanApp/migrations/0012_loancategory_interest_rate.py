# Generated by Django 5.0.4 on 2024-05-03 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loanApp', '0011_alter_customerloan_id_alter_loancategory_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='loancategory',
            name='interest_rate',
            field=models.FloatField(default=0.0),
        ),
    ]
# Generated by Django 5.0.4 on 2024-05-03 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loanApp', '0010_loantransaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerloan',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='loancategory',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='loanrequest',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

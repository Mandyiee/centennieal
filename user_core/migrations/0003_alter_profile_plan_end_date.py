# Generated by Django 4.1.4 on 2022-12-08 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_core', '0002_remove_profile_profit_list_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='plan_end_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

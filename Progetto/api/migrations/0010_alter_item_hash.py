# Generated by Django 4.1.6 on 2023-02-21 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_item_item_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='hash',
            field=models.CharField(default=None, max_length=64, null=True),
        ),
    ]

# Generated by Django 4.1.6 on 2023-02-21 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_item_hash_item_item_sumup_item_txid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_actions_number',
            field=models.IntegerField(default=0),
        ),
    ]

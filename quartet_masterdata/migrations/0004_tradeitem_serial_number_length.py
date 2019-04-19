# Generated by Django 2.0.4 on 2019-04-19 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quartet_masterdata', '0003_auto_20190305_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='tradeitem',
            name='serial_number_length',
            field=models.PositiveSmallIntegerField(help_text="The length of this material's serial number field", null=True, verbose_name='Serial Number Length'),
        ),
    ]
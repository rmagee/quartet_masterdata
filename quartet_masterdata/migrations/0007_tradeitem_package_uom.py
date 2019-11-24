# Generated by Django 2.2.3 on 2019-10-11 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quartet_masterdata', '0006_auto_20190812_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='tradeitem',
            name='package_uom',
            field=models.CharField(blank=True, help_text='The unit of measure for the packaged product, for exampleCS, Btl, etc.  Expectations will vary by integration.', max_length=5, null=True, verbose_name='Package UOM'),
        ),
    ]
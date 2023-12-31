# Generated by Django 3.0.2 on 2020-02-12 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quartet_masterdata', '0007_tradeitem_package_uom'),
    ]

    operations = [
        migrations.CreateModel(
            name='OutboundMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(help_text='The company to create the trading partner mapping for', on_delete=django.db.models.deletion.CASCADE, to='quartet_masterdata.Company', verbose_name='Company')),
                ('from_business', models.ForeignKey(blank=True, help_text='The default from company to use if the company is not used in the mapping.  Leave this blank if the company is always the business owner for outbound master data.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_from', to='quartet_masterdata.Company', verbose_name='Default From')),
                ('ship_from', models.ForeignKey(blank=True, help_text='The default ship from location for the company.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='location_from', to='quartet_masterdata.Location', verbose_name='Default Ship From')),
                ('ship_to', models.ForeignKey(blank=True, help_text='The default ship to location for the company.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='location_to', to='quartet_masterdata.Location', verbose_name='Default Ship To')),
                ('to_business', models.ForeignKey(blank=True, help_text='The default to which product shipments will be mapped if applicable.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_to', to='quartet_masterdata.Company', verbose_name='Default To Business')),
            ],
        ),
    ]

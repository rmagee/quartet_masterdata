# Generated by Django 2.2.3 on 2019-08-12 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quartet_masterdata', '0005_tradeitem_pack_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='GLN13',
            field=models.CharField(blank=True, db_index=True, help_text='The GLN (Global Location Number) provides a standard means to identify legal entities, trading parties and locations to support the requirements of electronic commerce. The GLN-13 is defined by GS1', max_length=13, null=True, unique=True, verbose_name='GLN13'),
        ),
        migrations.AlterField(
            model_name='company',
            name='SGLN',
            field=models.CharField(blank=True, db_index=True, help_text='The SGLN EPC scheme is used to assign a unique identity to a physical location or sub-location, such as a specific building or a specific unit of shelving within a warehouse.  TheSGLN is expressed as a URN value.', max_length=150, null=True, unique=True, verbose_name='SGLN'),
        ),
        migrations.AlterField(
            model_name='company',
            name='address1',
            field=models.CharField(blank=True, help_text='For example, the name of the street and the number in the street or the name of a building', max_length=1000, null=True, verbose_name='Street Address One'),
        ),
        migrations.AlterField(
            model_name='company',
            name='address2',
            field=models.CharField(blank=True, help_text='The second free form line complements the first free form line to locate the party or location.', max_length=1000, null=True, verbose_name='Street Address Two'),
        ),
        migrations.AlterField(
            model_name='company',
            name='address3',
            field=models.CharField(blank=True, help_text='The third free form line complements the first and second free form lines where necessary.', max_length=1000, null=True, verbose_name='Street Address Three'),
        ),
        migrations.AlterField(
            model_name='company',
            name='city',
            field=models.CharField(blank=True, help_text='City', max_length=50, null=True, verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_type',
            field=models.ForeignKey(blank=True, help_text='Describes the type of company.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='quartet_masterdata.CompanyType', verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='company',
            name='country',
            field=models.CharField(blank=True, help_text='Country ISO 3166-1 alpha-2 Code', max_length=2, null=True, verbose_name='Country Code'),
        ),
        migrations.AlterField(
            model_name='company',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, help_text=' Latitude of the location, in degrees. Positive numbers are northern latitude; negative numbers are southern latitude.', max_digits=9, null=True, verbose_name='Latitude'),
        ),
        migrations.AlterField(
            model_name='company',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, help_text='Longitude of the location, in degrees. Positive numbers are eastern longitude; negative numbers are western longitude.', max_digits=9, null=True, verbose_name='Longitude'),
        ),
        migrations.AlterField(
            model_name='company',
            name='postal_code',
            field=models.CharField(blank=True, help_text='Postal Code', max_length=20, null=True, verbose_name='Postal Code'),
        ),
        migrations.AlterField(
            model_name='company',
            name='state_province',
            field=models.CharField(blank=True, help_text='One of the constituent units of a nation having a federal government.', max_length=20, null=True, verbose_name='State or Province'),
        ),
        migrations.AlterField(
            model_name='location',
            name='GLN13',
            field=models.CharField(blank=True, db_index=True, help_text='The GLN (Global Location Number) provides a standard means to identify legal entities, trading parties and locations to support the requirements of electronic commerce. The GLN-13 is defined by GS1', max_length=13, null=True, unique=True, verbose_name='GLN13'),
        ),
        migrations.AlterField(
            model_name='location',
            name='SGLN',
            field=models.CharField(blank=True, db_index=True, help_text='The SGLN EPC scheme is used to assign a unique identity to a physical location or sub-location, such as a specific building or a specific unit of shelving within a warehouse.  TheSGLN is expressed as a URN value.', max_length=150, null=True, unique=True, verbose_name='SGLN'),
        ),
        migrations.AlterField(
            model_name='location',
            name='address1',
            field=models.CharField(blank=True, help_text='For example, the name of the street and the number in the street or the name of a building', max_length=1000, null=True, verbose_name='Street Address One'),
        ),
        migrations.AlterField(
            model_name='location',
            name='address2',
            field=models.CharField(blank=True, help_text='The second free form line complements the first free form line to locate the party or location.', max_length=1000, null=True, verbose_name='Street Address Two'),
        ),
        migrations.AlterField(
            model_name='location',
            name='address3',
            field=models.CharField(blank=True, help_text='The third free form line complements the first and second free form lines where necessary.', max_length=1000, null=True, verbose_name='Street Address Three'),
        ),
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.CharField(blank=True, help_text='City', max_length=50, null=True, verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='location',
            name='company',
            field=models.ForeignKey(blank=True, help_text='The company, if any, associated with this location.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='quartet_masterdata.Company', verbose_name='Company'),
        ),
        migrations.AlterField(
            model_name='location',
            name='country',
            field=models.CharField(blank=True, help_text='Country ISO 3166-1 alpha-2 Code', max_length=2, null=True, verbose_name='Country Code'),
        ),
        migrations.AlterField(
            model_name='location',
            name='icon',
            field=models.FileField(blank=True, help_text='An icon to represent the location in a GUI or report.', null=True, upload_to='qu4rtetmasterdataimages/', verbose_name='Icon'),
        ),
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, help_text=' Latitude of the location, in degrees. Positive numbers are northern latitude; negative numbers are southern latitude.', max_digits=9, null=True, verbose_name='Latitude'),
        ),
        migrations.AlterField(
            model_name='location',
            name='location_type',
            field=models.ForeignKey(blank=True, help_text='An additional classifier that can be used to identifythe location outside of the CBV codes.  This can be an internal classifier or a human readable that lends further clarity to the location record.', null=True, on_delete=django.db.models.deletion.CASCADE, to='quartet_masterdata.LocationType', verbose_name='Location Type'),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, help_text='Longitude of the location, in degrees. Positive numbers are eastern longitude; negative numbers are western longitude.', max_digits=9, null=True, verbose_name='Longitude'),
        ),
        migrations.AlterField(
            model_name='location',
            name='postal_code',
            field=models.CharField(blank=True, help_text='Postal Code', max_length=20, null=True, verbose_name='Postal Code'),
        ),
        migrations.AlterField(
            model_name='location',
            name='site',
            field=models.ForeignKey(blank=True, help_text='Identifies the site in which this location is contained...if at all. For a Sub-site location, this is the identifier of the parent location.', null=True, on_delete=django.db.models.deletion.CASCADE, to='quartet_masterdata.Location', verbose_name='Site'),
        ),
        migrations.AlterField(
            model_name='location',
            name='ssa',
            field=models.CharField(blank=True, help_text='Sub-Site Attribute: further qualifies the business function of the sub-site location. This master data attribute is only applicable to a sub-site location. Sub-site attributes are expressed as a comma- separated list of zero or more numerical codes', max_length=1000, null=True, verbose_name='Sub-Site Attribute'),
        ),
        migrations.AlterField(
            model_name='location',
            name='sst',
            field=models.SmallIntegerField(blank=True, help_text='Sub-Site Type: describes the primary business function of the sub-site location. This master data attribute is only applicable to a sub-site location.  This value is expressed as a single numerical code.', null=True, verbose_name='Sub-Site Type'),
        ),
        migrations.AlterField(
            model_name='location',
            name='state_province',
            field=models.CharField(blank=True, help_text='One of the constituent units of a nation having a federal government.', max_length=20, null=True, verbose_name='State or Province'),
        ),
        migrations.AlterField(
            model_name='locationfield',
            name='description',
            field=models.CharField(blank=True, help_text='A short description.', max_length=500, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='locationidentifier',
            name='description',
            field=models.CharField(blank=True, help_text='A brief description of what the identifier represents.', max_length=150, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='measurement_unit_code',
            field=models.CharField(blank=True, help_text='The unit of measure for the measurement. The code list for this attribute is UN/ECE Recommendation 20', max_length=40, null=True, verbose_name='measurement_unit_code'),
        ),
        migrations.AlterField(
            model_name='tradeitem',
            name='NDC',
            field=models.CharField(blank=True, help_text='The national drug code for the product. US Only.', max_length=12, null=True, verbose_name='NDC'),
        ),
        migrations.AlterField(
            model_name='tradeitem',
            name='NDC_pattern',
            field=models.CharField(blank=True, choices=[('4-4-2', '4-4-2'), ('5-3-2', '5-3-2'), ('5-4-1', '5-4-1')], help_text='The pattern of the NDC.  US Only.  Optional.', max_length=5, null=True, verbose_name='NDC_pattern'),
        ),
        migrations.AlterField(
            model_name='tradeitem',
            name='additional_id',
            field=models.CharField(blank=True, help_text='A trade item identifier that is in addition to the GTIN.', max_length=80, null=True, verbose_name='Additional ID'),
        ),
        migrations.AlterField(
            model_name='tradeitem',
            name='additional_id_typecode',
            field=models.CharField(blank=True, help_text='The code list for this attribute is defined in GS1 GDSN.', max_length=250, null=True, verbose_name='Additional ID TypeCode'),
        ),
        migrations.AlterField(
            model_name='tradeitem',
            name='country_of_origin',
            field=models.CharField(blank=True, help_text='Country from which the goods are supplied. The code list for this attribute is the ISO 3166-1 Alpha-2 list of 2-letter country codes', max_length=2, null=True, verbose_name='Country Of Origin'),
        ),
        migrations.AlterField(
            model_name='tradeitem',
            name='description_short',
            field=models.CharField(blank=True, help_text='A free form short length description of the trade item that can be used to identify the trade item at point of sale.', max_length=35, null=True, verbose_name='description_short'),
        ),
        migrations.AlterField(
            model_name='tradeitem',
            name='dosage_form_type',
            field=models.CharField(blank=True, help_text='A dosage form is the physical form of a medication that identifies the form of the pharmaceutical item. For example: PILL', max_length=35, null=True, verbose_name='Dosage Form Type'),
        ),
        migrations.AlterField(
            model_name='tradeitem',
            name='drained_weight',
            field=models.FloatField(blank=True, help_text='The weight of the trade item when drained of its liquid. For example 225 grm', null=True, verbose_name='Drained Weight'),
        ),
        migrations.AlterField(
            model_name='tradeitem',
            name='drained_weight_uom',
            field=models.CharField(blank=True, help_text='The unit of measure for the drained weight as defined inUN/ECE Recommendation 20.', max_length=5, null=True, verbose_name='Drained Weight UOM'),
        ),
        migrations.AlterField(
            model_name='tradeitem',
            name='functional_name',
            field=models.CharField(blank=True, help_text='Describes use of the product or service by the consumer. Should help clarify the product classification associated with the GTIN.', max_length=100, null=True, verbose_name='functional_name'),
        ),
        migrations.AlterField(
            model_name='tradeitem',
            name='gross_weight',
            field=models.FloatField(blank=True, help_text='Used to identify the gross weight of the trade item. The gross weight includes all packaging materials of the trade item.', null=True, verbose_name='Gross Weight'),
        ),
        migrations.AlterField(
            model_name='tradeitem',
            name='gross_weight_uom',
            field=models.CharField(blank=True, help_text='The unit of measure for the gross weight as defined inUN/ECE Recommendation 20.', max_length=5, null=True, verbose_name='Gross Weight UOM'),
        ),
        migrations.AlterField(
            model_name='tradeitem',
            name='image',
            field=models.FileField(blank=True, help_text='An image to represent the product in a GUI or report.', null=True, upload_to='qu4rtetmasterdataimages/', verbose_name='Icon'),
        ),
        migrations.AlterField(
            model_name='tradeitem',
            name='label_description',
            field=models.CharField(blank=True, help_text="A literal reproduction of the text featured on a product's label in the same word-by-word order in which it appears on the front of the product's packaging.", max_length=500, null=True, verbose_name='Label Description'),
        ),
        migrations.AlterField(
            model_name='tradeitem',
            name='manufacturer_name',
            field=models.CharField(blank=True, help_text='Party name information for the manufacturer of the trade item. Example: Acme Corporation', max_length=300, null=True, verbose_name='manufacturer_name'),
        ),
        migrations.AlterField(
            model_name='tradeitem',
            name='net_content_description',
            field=models.CharField(blank=True, help_text='Free text describing the amount of the trade item contained by a package, usually as claimed on the label. Example: 253 grams', max_length=500, null=True, verbose_name='Net Content Description'),
        ),
        migrations.AlterField(
            model_name='tradeitem',
            name='net_weight',
            field=models.FloatField(blank=True, help_text='Used to identify the net weight of the trade item. Net weight excludes any packaging materials and applies to all levels but consumer unit level.', null=True, verbose_name='Net Weight'),
        ),
        migrations.AlterField(
            model_name='tradeitem',
            name='net_weight_uom',
            field=models.CharField(blank=True, help_text='The unit of measure for the net weight as defined inUN/ECE Recommendation 20.', max_length=5, null=True, verbose_name='NET Weight UOM'),
        ),
        migrations.AlterField(
            model_name='tradeitem',
            name='pack_count',
            field=models.PositiveIntegerField(blank=True, help_text='The number of items packed into this package (where appropriate).', null=True, verbose_name='Pack Count'),
        ),
        migrations.AlterField(
            model_name='tradeitem',
            name='regulated_product_name',
            field=models.CharField(blank=True, help_text='The prescribed, regulated or generic product name or denomination that describes the true nature of the product according to country specific regulation.', max_length=500, null=True, verbose_name='regulated_product_name'),
        ),
        migrations.AlterField(
            model_name='tradeitem',
            name='serial_number_length',
            field=models.PositiveSmallIntegerField(blank=True, help_text="The length of this material's serial number field", null=True, verbose_name='Serial Number Length'),
        ),
        migrations.AlterField(
            model_name='tradeitem',
            name='strength_description',
            field=models.CharField(blank=True, help_text='Free text describing the strength of the active ingredient(s) of the product. Example: 200mg/100mg', max_length=500, null=True, verbose_name='strength_description'),
        ),
        migrations.AlterField(
            model_name='tradeitem',
            name='trade_item_description',
            field=models.CharField(blank=True, help_text='An understandable and useable description of a trade item using brand and other descriptors.', max_length=200, null=True, verbose_name='Trade Item Description'),
        ),
        migrations.AlterField(
            model_name='tradeitemfield',
            name='description',
            field=models.CharField(blank=True, help_text='A short description.', max_length=500, null=True, verbose_name='Description'),
        ),
    ]

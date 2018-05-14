# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import gettext_lazy as _


class Field(models.Model):
    '''
    An abstract name/value pair model
    '''
    name = models.CharField(
        max_length=100,
        null=False,
        db_index=True,
        help_text=_('The name of the field.'),
        verbose_name=_('Name')
    )
    value = models.TextField(
        help_text=_('The value of the field.'),
        verbose_name=_('Value')
    )
    description = models.CharField(
        max_length=500,
        null=True,
        help_text=_('A short description.'),
        verbose_name=_('Description')
    )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class GenericType(models.Model):
    identifier = models.CharField(
        max_length=20,
        db_index=True,
        verbose_name=_("Identifier"),
        help_text=_("The unique type identifier."),
        null=False
    )
    description = models.CharField(
        max_length=400,
        verbose_name=_("Description"),
        help_text=_("A brief description of the type."),
        null=False
    )

    def __str__(self):
        return self.identifier

    class Meta:
        abstract = True


class Address(models.Model):
    '''
    Defines a mailing address for a location.
    '''
    address1 = models.CharField(
        max_length=400,
        verbose_name=_("address1"),
        help_text=_("Street Address"),
        null=True
    )
    address2 = models.CharField(
        max_length=400,
        verbose_name=_("address2"),
        help_text=_("Street Address 2"),
        null=True
    )
    country = models.CharField(
        max_length=2,
        verbose_name=_("Country"),
        help_text=_("Country ISO 3166-1 alpha-2 Code"),
        null=True
    )
    city = models.CharField(
        max_length=50,
        verbose_name=_("city"),
        help_text=_("City"),
        null=True
    )
    state_province = models.CharField(
        max_length=10,
        verbose_name=_("State or Province"),
        help_text=_("State or Province"),
        null=True
    )
    postal_code = models.CharField(
        max_length=20,
        verbose_name=_("Postal Code"),
        help_text=_("Postal Code"),
        null=True
    )

    def __str__(self):
        return "%s %s, %s, %s, %s, %s" % (
            self.address1,
            self.address2,
            self.country,
            self.city,
            self.state_province,
            self.postal_code
        )

    class Meta:
        abstract = True


class Location(Address):
    '''
    Defines a physical location.
    '''
    name = models.CharField(
        max_length=100,
        verbose_name=_("Name"),
        help_text=_("A unique name for the location."),
        db_index=True,
        null=False,
        unique=True
    )
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        verbose_name=_("Latitude"),
        help_text=_("Latitude"),
        null=True
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        verbose_name=_("Longitude"),
        help_text=_("Longitude"),
        null=True
    )
    location_type = models.ForeignKey(
        'quartet_masterdata.LocationType',
        help_text=_("Location Type"),
        verbose_name=_("The type of location."),
        null=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Location')
        verbose_name_plural = _('Locations')


class LocationField(Field):
    '''
    Assignable name-value fields can be added to locations.
    '''
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Location Field')
        verbose_name_plural = _('Location Fields')


class LocationIdentifier(models.Model):
    '''
    A location may have one or more unique identifiers.  This allows for
    a location to have one GLN-13 for example and another internal identifier
    should that be the case.
    '''
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE
    )
    identifier = models.CharField(
        max_length=250,
        verbose_name=_("identifier"),
        help_text=_("A unique identifier for a location such as a GLN "
                    "or SGLN."),
        null=False
    )
    identifier_type = models.CharField(
        max_length=50,
        verbose_name=_("identifier_type"),
        help_text=_("The type of location identifier. For example: GLN-13, "
                    "SGLN, etc."),
        null=False
    )

    class Meta:
        verbose_name = _('LocationIdentifier')
        verbose_name_plural = _('LocationIdentifiers')


class LocationType(GenericType):
    '''
    Notes the type of location.  For example, Plant, Campus, Customer,
    Warehouse, etc.
    '''

    class Meta:
        verbose_name = _('Location Type')
        verbose_name_plural = _('Location Types')


class Measurement(models.Model):
    '''
    Based on the measurement specifics in the GS1 CBV 1.2 in section
    9.2.4
    '''
    measurement = models.FloatField(
        null=False,
        help_text=_('The numerical value of the measurement'),
        verbose_name=_('Measurement')
    )
    measurement_unit_code = models.CharField(
        max_length=40,
        verbose_name=_("measurement_unit_code"),
        help_text=_("The unit of measure for the measurement. The code list "
                    "for this attribute is UN/ECE Recommendation 20"),
        null=True
    )

    def __str__(self):
        return "%s: %s" % (self.measurement, self.measurement_unit_code)


class ItemInstance(models.Model):
    '''
    Base class for Trade Items and Instance Level models.
    '''
    country_of_origin = models.CharField(
        max_length=2,
        verbose_name=_("Country Of Origin"),
        help_text=_("Country from which the goods are supplied. The code list "
                    "for this attribute is the ISO 3166-1 Alpha-2 list "
                    "of 2-letter country codes"),
        null=True
    )
    drained_weight = models.ForeignKey(
        Measurement,
        verbose_name=_('Drained Weight'),
        help_text=_('The weight of the trade item when drained of its '
                    'liquid. For example 225 "grm'),
        null=True,
        on_delete=models.CASCADE
    )
    gross_weight = models.ForeignKey(
        Measurement,
        verbose_name=_('Gross Weight'),
        help_text=_('Used to identify the gross weight of the trade item. '
                    'The gross weight includes all packaging materials '
                    'of the trade item.'),
        null=True,
        on_delete=models.CASCADE
    )
    net_weight = models.ForeignKey(
        Measurement,
        verbose_name=_('Net Weight'),
        null=True,
        on_delete=models.CASCADE
    )
    class Meta:
        abstract = True


class TradeItem(ItemInstance):
    '''
    Based on the GS1 CBV 1.2 Trade Item Master Data Attributes in section
    9 of the standard.
    '''
    additional_id = models.CharField(
        max_length=80,
        verbose_name=_("Additional ID"),
        help_text=_(
            "A trade item identifier that is in addition to the GTIN."),
        null=True
    )
    additional_id_typecode = models.CharField(
        max_length=250,
        verbose_name=_("Additional ID TypeCode"),
        help_text=_(
            "The code list for this attribute is defined in GS1 GDSN."),
        null=True
    )
    description_short = models.CharField(
        max_length=35,
        verbose_name=_("description_short"),
        help_text=_("A free form short length description of the trade item "
                    "that can be used to identify the trade item at "
                    "point of sale."),
        null=True
    )
    dosage_form_type = models.CharField(
        max_length=35,
        verbose_name=_("Dosage Form Type"),
        help_text=_("A dosage form is the physical form of a medication "
                    "that identifies the form of the pharmaceutical item."
                    " For example: PILL"),
        null=True
    )
    functional_name = models.CharField(
        max_length=100,
        verbose_name=_("functional_name"),
        help_text=_("Describes use of the product or service by the consumer. "
                    "Should help clarify the product classification"
                    " associated with the GTIN."),
        null=True
    )
    manufacturer_name = models.CharField(
        max_length=300,
        verbose_name=_("manufacturer_name"),
        help_text=_("Party name information for the manufacturer of the trade "
                    "item. Example: Acme Corporation"),
        null=True
    )
    net_content_description = models.CharField(
        max_length=500,
        verbose_name=_("Net Content Description"),
        help_text=_("Free text describing the amount of the trade item "
                    "contained by a package, usually as claimed on the label. "
                    "Example: 253 grams"),
        null=True
    )
    label_description = models.CharField(
        max_length=500,
        verbose_name=_("Label Description"),
        help_text=_("A literal reproduction of the text featured on a "
                    "product's label in the same word-by-word order in which "
                    "it appears on the front of the product's packaging."),
        null=True
    )
    regulated_product_name = models.CharField(
        max_length=500,
        verbose_name=_("regulated_product_name"),
        help_text=_("The prescribed, regulated or generic product name or "
                    "denomination that describes the true nature of the "
                    "product "
                    "according to country specific regulation."),
        null=True
    )
    strength_description = models.CharField(
        max_length=500,
        verbose_name=_("strength_description"),
        help_text=_("Free text describing the strength of the active "
                    "ingredient(s) of the product. Example: 200mg/100mg"),
        null=True
    )
    trade_item_description = models.CharField(
        max_length=200,
        verbose_name=_("Trade Item Description"),
        help_text=_("An understandable and useable description of a trade "
                    "item using brand and other descriptors."),
        null=True
    )
    class Meta:
        abstract = True

class TradeItemInstance(ItemInstance):
    '''
    From section 9.2.3 of the CBV 1.2 spec.
    '''
    lot_number = models.CharField(
        max_length=20,
        verbose_name=_("Lot Number"),
        help_text=_("The Lot Number"),
        null=True
    )

class Material(models.Model):
    pass


class MaterialUOM(models.Model):
    pass


class MaterialField(models.Model):
    pass


class MaterialIdentifier(models.Model):
    pass


class Entity(models.Model):
    pass


class EntityType(models.Model):
    pass


class EntityIdentifier(models.Model):
    pass


class EntityField(models.Model):
    pass

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

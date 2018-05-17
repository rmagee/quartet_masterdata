# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright 2018 SerialLab Corp.  All rights reserved.
from quartet_masterdata import models
import factory


class LocationTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.LocationType

    identifier = 'BSS'
    description = 'Baseball Stadium'


class LocationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Location

    GLN13 = '3055551234561'
    SGLN = 'urn:epc:id:sgln:305555.123456.0'
    name = "Headquarters"
    address1 = 'One Citizens Bank Way'
    country = 'US'
    city = 'Philadelphia'
    state_province = 'PA'
    postal_code = '19148'
    latitude = '39.906098'
    longitude = '-75.165733'
    location_type = factory.Iterator(models.LocationType.objects.all())


class LocationFieldFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.LocationField

    name = 'Internal Code'
    value = 'PL72'
    description = 'Internal plant code #72.'
    location = factory.Iterator(models.Location.objects.all())


class LocationIdentifierFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.LocationIdentifier

    identifier = 'urn:epc:id:sgln:305555.123456.1'
    identifier_type = 'SGLN'
    description = 'First Base'
    location = factory.Iterator(models.Location.objects.all())


class TradeItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.TradeItem

    country_of_origin = 'US'
    drained_weight = None
    gross_weight = 10.5
    gross_weight_uom = 'LBR'
    net_weight = 10
    net_weight_uom = 'LBR'
    GTIN14 = '12341234123411'
    NDC = '1234-1234-12'
    NDC_pattern = '4-4-2'
    additional_id = '45039-33'
    additional_id_typecode = 'GST'
    description_short = 'Supressitol'
    dosage_form_type = 'PILL'
    functional_name = 'Widget'
    manufacturer_name = 'Acme Corp.'
    net_content_description = '600 grams'
    label_description = 'Supressitol Tablets: 10 grams of suppression.'
    regulated_product_name = 'Supressitoxide Carbonite'
    strength_description = '100mg'
    trade_item_description = 'Supressitol Brand Suppression Tablets'


class TradeItemFieldFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.TradeItemField

    trade_item = factory.Iterator(models.TradeItem.objects.all())
    name = 'MATNO'
    value = '32423-33-333'
    description = 'SAP Internal Material Number'





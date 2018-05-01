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

    identifier = 'urn:epc:id:sgln:305555.123456.0'
    identifier_type = 'SGLN'
    location = factory.Iterator(models.Location.objects.all())

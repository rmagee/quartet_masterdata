#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_quartet_masterdata
------------

Tests for `quartet_masterdata` models module.
"""

from django.test import TestCase

from quartet_masterdata import models


class TestQuartet_Masterdata(TestCase):

    def setUp(self):
        from tests import factories
        location_type = factories.LocationTypeFactory.create()
        location = factories.LocationFactory.create()
        location2 = factories.LocationFactory.create(name='test', latitude=12.232,
                                                     longitude=33.2343)
        location_field = factories.LocationFieldFactory.create()
        location_identifier = factories.LocationIdentifierFactory.create()

    def test_create_plant(self):
        location = models.Location.objects.select_related(
            'location_type',
        ).prefetch_related(
            'locationfield_set',
            'locationidentifier_set'
        ).get(locationidentifier__identifier='urn:epc:id:sgln:305555.123456.0')

    def tearDown(self):
        pass

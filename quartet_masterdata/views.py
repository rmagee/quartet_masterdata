# -*- coding: utf-8 -*-
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

from rest_framework.response import Response
from rest_framework import views, status
from quartet_masterdata import models, serializers


class LocationByIdentifierView(views.APIView):
    '''
    Returns a Location detail record based on the inbound identifier.
    '''

    def get(self, request, format=None, identifier=None):
        try:
            location = models.Location.objects.select_related(
                'location_type',
            ).prefetch_related(
                'locationfield_set',
                'locationidentifier_set'
            ).get(
                SGLN=identifier
            )
            serializer = serializers.LocationSerializer(location)
            return Response(serializer.data)
        except models.Location.DoesNotExist:
            response = Response(
                'The location with identifier %s could not '
                'be found.' % identifier,
                status=status.HTTP_404_NOT_FOUND
            )
        return response

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

from rest_framework.serializers import ModelSerializer
from quartet_masterdata import models


class LocationFieldSerializer(ModelSerializer):
    '''
    Default serializer for the LocationField model.
    '''

    class Meta:
        model = models.LocationField
        fields = '__all__'


class LocationTypeSerializer(ModelSerializer):
    '''
    Default serializer for the LocationType model.
    '''

    class Meta:
        model = models.LocationType
        fields = '__all__'


class LocationIdentifierSerializer(ModelSerializer):
    '''
    Default serializer for the LocationIdentifier model.
    '''
    class Meta:
        model = models.LocationIdentifier
        fields = '__all__'


class LocationSerializer(ModelSerializer):
    '''
    Default serializer for the Location Model
    '''
    #location_type = LocationTypeSerializer(many=False, read_only=True)
    locationidentifier_set = LocationIdentifierSerializer(many=True, read_only=True)
    locationfield_set = LocationFieldSerializer(many=True, read_only=True)

    class Meta:
        model = models.Location
        fields = '__all__'

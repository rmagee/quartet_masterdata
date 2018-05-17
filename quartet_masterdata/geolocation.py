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
from datetime import datetime
from typing import List

class GeoEvent:
    '''
    Used as a result structure for geo history queries
    '''
    def __init__(self, biz_location: str = None, event_time: datetime = None,
                 longitude: float = None, latitude: float = None):
        self._biz_location = biz_location
        self._event_time = event_time
        self._longitude = longitude
        self._latitude = latitude

    @property
    def biz_location(self):
        return self._biz_location

    @biz_location.setter
    def biz_location(self, value):
        self._biz_location = value

    @property
    def event_time(self):
        return self._event_time

    @event_time.setter
    def event_time(self, value):
        self._event_time = value

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value

# typed list for code hints, etc
GeoEventList = List[GeoEvent]

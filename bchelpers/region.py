# Copyright 2014 Mitch Garnaat
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import botocore.session
from bchelpers.serviceendpoint import ServiceEndpoint


class Region(object):
    """
    Represents a specific region and a specific set of credentials.
    Using the ``Region`` object you can then create ``ServiceEndpoints``
    to talk to a specific service within that region and using those
    credentials.

    :type region_name: str
    :param region_name: The name of the region (e.g. us-east-1).

    :type profile: str
    :param profile: The profile you wish to associate with this
        object.  This can be any valid profile within your botocore
        config file.  If no profile is specified, the default profile
        is used.
    """

    def __init__(self, region_name, profile=None):
        self.session = botocore.session.get_session()
        self.session.profile = profile
        self.region_name = region_name

    def __repr__(self):
        return self.region_name

    def debug(self):
        self.session.set_debug_logger()

    def get_service_endpoint(self, service_name):
        """
        Returns a ``ServiceEndpoint`` object for a particular service
        within this region using the credentials specified in the
        profile associated with this object.

        :type service_name: str
        :param service_name: The name of the service you wish to
            connect to (e.g. ec2).
        """
        service = self.session.get_service(service_name)
        endpoint = service.get_endpoint(self.region_name)
        return ServiceEndpoint(self, service, endpoint)

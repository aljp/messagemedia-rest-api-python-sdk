# coding: utf-8

"""
    MessageMedia REST API

    Australia's Leading Messaging Solutions for Business and Enterprise.

    OpenAPI spec version: 1.0.0
    Contact: support@messagemedia.com

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class MetadataKeysResponseProperties(object):
    """
    Do not edit the class manually.
    """
    def __init__(self, end_date=None, start_date=None, accounts=None):
        """
        MetadataKeysResponseProperties - a model

        :param dict types: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.types = {
            'end_date': 'datetime',
            'start_date': 'datetime',
            'accounts': 'list[str]'
        }

        self.attribute_map = {
            'end_date': 'end_date',
            'start_date': 'start_date',
            'accounts': 'accounts'
        }

        self._end_date = end_date
        self._start_date = start_date
        self._accounts = accounts

    @property
    def end_date(self):
        """
        Gets the end_date of this MetadataKeysResponseProperties.
        The end date provided as a parameter for this report

        :return: The end_date of this MetadataKeysResponseProperties.
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this MetadataKeysResponseProperties.
        The end date provided as a parameter for this report

        :param end_date: The end_date of this MetadataKeysResponseProperties.
        :type: datetime
        """

        self._end_date = end_date

    @property
    def start_date(self):
        """
        Gets the start_date of this MetadataKeysResponseProperties.
        The end date provided as a parameter for this report

        :return: The start_date of this MetadataKeysResponseProperties.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this MetadataKeysResponseProperties.
        The end date provided as a parameter for this report

        :param start_date: The start_date of this MetadataKeysResponseProperties.
        :type: datetime
        """

        self._start_date = start_date

    @property
    def accounts(self):
        """
        Gets the accounts of this MetadataKeysResponseProperties.
        List of accounts that were considered when fetching the metadata keys.

        :return: The accounts of this MetadataKeysResponseProperties.
        :rtype: list[str]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """
        Sets the accounts of this MetadataKeysResponseProperties.
        List of accounts that were considered when fetching the metadata keys.

        :param accounts: The accounts of this MetadataKeysResponseProperties.
        :type: list[str]
        """

        self._accounts = accounts

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

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

from __future__ import absolute_import

import os
import sys
import unittest

import messagemedia_rest_api
from messagemedia_rest_api.rest import ApiException
from messagemedia_rest_api.models.received_messages import ReceivedMessages


class TestReceivedMessages(unittest.TestCase):
    """ ReceivedMessages unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testReceivedMessages(self):
        """
        Test ReceivedMessages
        """
        model = messagemedia_rest_api.models.received_messages.ReceivedMessages()


if __name__ == '__main__':
    unittest.main()

import unittest
from zcddbclient import ddb_client
from decimal import Decimal


class DdbClientTests(unittest.TestCase):

    # TODO:
    #   add assertions
    #   add setUp and tearDown methods
    #   add more tests
    #   automate testing with Tox

    # TODO: in the setUp() method:
    #   setup the aws credentials and config files programmatically
    #   can I mock the connection to DynamoDB?

    def test_create_item(self):
        ddb_client.write_item(
            qualifier="speed_test",
            device_id="rasp_pi",
            location="Home",
            value="100",
            unit="Mbps"
        )

    def test_create_item_float_value(self):
        ddb_client.write_item(
            qualifier="speed_test_2",
            device_id="rasp_pi",
            location="Home",
            value="10.984598",
            unit="Mbps"
        )

    def test_create_item_invalid_value(self):
        self.assertRaises(
            ValueError,
            ddb_client.write_item,
            qualifier="speed_test_2",
            device_id="rasp_pi",
            location="Home",
            value="this is not a number",
            unit="Mbps"
        )

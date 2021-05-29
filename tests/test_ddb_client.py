import unittest
from zcddbclient import ddb_client


class DdbClientTests(unittest.TestCase):

    def test_create_new_item_in_table(self):
        ddb_client.write_item(
            qualifier="speed_test",
            device_id="rasp_pi",
            location="Home",
            value="100",
            unit="Mbps"
        )

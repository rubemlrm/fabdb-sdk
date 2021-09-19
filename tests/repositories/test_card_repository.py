import json
import unittest

from fabdb_sdk.exceptions.not_found_exception import NotFoundException
from fabdb_sdk.repositories.card_repository import CardRepository


class Test_TestCardRepository(unittest.TestCase):
    def test_get_all(self):
        response = CardRepository().get_all()
        self.assertIn("absorb-in-aether-blue", json.dumps(response), "not found")

    def test_get_card(self):
        response = CardRepository().get_card("ARC000")
        self.assertEqual(response.name, "Eye of Ophidia")

    def test_get_invalid_card(self):
        with self.assertRaises(NotFoundException):
            CardRepository().get_card("ZZZ9999")

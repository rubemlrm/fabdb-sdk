# -*- coding: utf-8 -*-

import unittest

from fabdb_sdk.enums.rarity_enum import RarityEnum


class Test_TestRarityEnum(unittest.TestCase):

    def test_invalid_enum_value(self):
        self.assertFalse(RarityEnum.is_valid('Z'))

    def test_valid_enum_value(self):
        self.assertTrue(RarityEnum.is_valid('TOKEN'))

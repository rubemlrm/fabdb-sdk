# -*- coding: utf-8 -*-

import unittest

from fabdb_sdk.enums.expansion_set_enum import ExpansionSetEnum


class Test_TestExpansionSetEnum(unittest.TestCase):
    def test_invalid_enum_value(self):
        self.assertFalse(ExpansionSetEnum.is_valid("TEST"))

    def test_valid_enum_value(self):
        self.assertTrue(ExpansionSetEnum.is_valid("MON"))

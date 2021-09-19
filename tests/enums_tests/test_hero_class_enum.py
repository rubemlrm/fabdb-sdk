# -*- coding: utf-8 -*-

import unittest

from fabdb_sdk.enums.hero_class_enum import HeroClassEnum


class Test_TestHeroClassEnum(unittest.TestCase):
    def test_invalid_enum_value(self):
        self.assertFalse(HeroClassEnum.is_valid("TEST"))

    def test_valid_enum_value(self):
        self.assertTrue(HeroClassEnum.is_valid("GUARDIAN"))

# -*- coding: utf-8 -*-

from fabdb_sdk.enums.hero_class_enum import HeroClassEnum


class Test_TestHeroClassEnum():

    def test_invalid_enum_value(self):
        assert HeroClassEnum.is_valid('TEST') == False

    def test_valid_enum_value(self):
        assert HeroClassEnum.is_valid('GUARDIAN') == True

# -*- coding: utf-8 -*-

from fabdb_sdk.enums.rarity_enum import RarityEnum

class Test_TestRarityEnum():

    def test_invalid_enum_value(self):
        assert RarityEnum.is_valid('Z') == False

    def test_valid_enum_value(self):
        assert RarityEnum.is_valid('TOKEN') == True

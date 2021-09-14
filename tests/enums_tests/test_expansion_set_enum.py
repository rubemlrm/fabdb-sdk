# -*- coding: utf-8 -*-

from fabdb_sdk.enums.expansion_set_enum import ExpansionSetEnum


class Test_TestExpansionSetEnum():

    def test_invalid_enum_value(self):
        assert ExpansionSetEnum.is_valid('TEST') == False

    def test_valid_enum_value(self):
        assert ExpansionSetEnum.is_valid('MON') == True

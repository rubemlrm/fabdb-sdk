# -*- coding: utf-8 -*-

class Card:
    """Card Structure"""

    @property
    def identifier(self):
        return self.identifier

    @property.setter
    def identifier(self, value):
        self._identifier = value

    @property
    def name(self):
        return self.name

    @property.setter
    def name(self, value):
        self._name = value

    @property
    def rarity(self):
        """docstring for rarity"""
        return self.rarity

    @property.setter
    def rarity(self, value):
        self._rarity = value

    @property
    def keywords(self):
        return self.keywords

    @property.setter
    def keywords(self, value):
        self._keywords = value

    @property
    def stats(self):
        return self.stats

    @property.setter
    def stats(self,value):
        self._stats = value

    @property
    def text(self):
        return self.text

    @property.setter
    def text(self, value):
        self._text = value

    @property
    def flavour(self):
        return self.flavour

    @property.setter
    def flavour(self, value):
        self._flavour = value

    @property
    def comments(self):
        return self.comments

    @property.setter
    def comments(self):
        self._comments = value

    @property
    def banned(self):
        return self.banned

    @property.setter
    def banned(self, value):
        self._banned = value

    @property
    def image(self):
        return self.image

    @property.setter
    def image(self, value):
        return self._image = value

    @property
    def rullings(self):
        return self.rullings

    @property.setter
    def rullings(self, value):
        self._rullings = value



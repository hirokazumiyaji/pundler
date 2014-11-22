# coding: utf-8
from __future__ import absolute_import
from .base import Base


class List(Base):

    def run(self):
        import pip
        result = pip.main(['list'])

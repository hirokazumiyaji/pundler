# coding: utf-8
from __future__ import absolute_import
from .base import Base


class Install(Base):

    def __init__(self, config):
        self.config = config

    def run(self):
        for package in self.config.packages:
            package.install()

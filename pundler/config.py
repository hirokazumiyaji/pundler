# coding: utf-8
from __future__ import absolute_import
import os
import yaml
from .exceptions import EnvironmentNotFound, FileNotFound
from .package import Package


class Config(object):

    def __init__(self, pyfile=None, environment='development'):
        if pyfile:
            self.pyfile = pyfile
        else:
            self.pyfile = os.path.join(os.getcwd(), 'Pyfile')

        self._check_file(self.pyfile)

        self.data = yaml.load(open(self.pyfile).read())
        self.environment = environment

    @property
    def packages(self):
        if self.environment not in self.data:
            raise EnvironmentNotFound(
                'not environment({}) in config file Pyfile'.format(
                    self.environment))

        return [
            Package(name, config)
            for name, config in self.data[self.environment].iteritems()
        ]

    def _check_file(self, filepath):
        if not os.path.exists(filepath):
            raise FileNotFound('config file({}) not found.'.format(filepath))

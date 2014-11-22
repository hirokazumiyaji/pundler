# coding: utf-8
from __future__ import absolute_import
from optparse import OptionParser


class Parser(object):

    def __init__(self):
        self.parser = OptionParser()
        self.parser.add_option('-f',
                               '--file',
                               dest='filename',
                               help='config file path')
        self.parser.add_option('-e',
                               '--environment',
                               dest='environment',
                               help='config environment')

    def parse(self):
        return self.parser.parse_args()

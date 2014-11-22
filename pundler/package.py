# coding: utf-8
from __future__ import absolute_import


class Package(object):

    def __init__(self, name, config):
        self.name = name

        if config:
            self.version = config.get('version')
            self.repository_url = config.get('git') or \
                config.get('svn') or config.get('hg')
        else:
            self.version = None
            self.repository_url = None

    @property
    def option(self):
        if self.version:
            if '=' in self.version:
                return '{}{}'.format(self.name, self.version)
            elif '>' in self.version:
                return '{}{}'.format(self.name, self.version)
            elif '<' in self.version:
                return '{}{}'.format(self.name, self.version)
            else:
                return '{}=={}'.format(self.name, self.version)

        elif self.repository_url:
            return 'git+{}'.format(self.repository_url)

        else:
            return self.name

    def install(self):
        import pip
        print('\033[32mpip install {}...\033[0m'.format(self.name))
        if self.repository_url:
            result = pip.main(['install', '-e', self.option])
        else:
            result = pip.main(['install', self.option, '--no-use-wheel'])
        return result

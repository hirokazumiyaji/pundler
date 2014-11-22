# coding: utf-8


class BaseError(Exception):
    pass


class NotCommandError(BaseError):
    pass


class FileNotFound(BaseError):
    pass


class EnvironmentNotFound(BaseError):
    pass

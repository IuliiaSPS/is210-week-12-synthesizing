#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_01"""


class BaseError(Exception):
    """Base class."""
    pass


class StringError(BaseError, TypeError):
    """Class to inherit from Base class and TypeError class."""
    pass


class NumberError(BaseError, TypeError):
    """Class to inherit from Base class and TypeError class."""
    pass


class NonZeroError(NumberError):
    """Class to inherit from NumberError class."""
    pass

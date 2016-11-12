#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_02"""


class CustomError(Exception):
    """Custom Exception subclass."""

    def __init__(self, message, cause):
        """Constructor for CustomError class.

        Args:
            message(optional): user input.
            cause(optional): user input

        Attributes:
            message(optional): user input.
            cause(optional): user input
        """

        Exception.__init__(self, message)
        self.cause = cause

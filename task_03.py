#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


def exception_test(arg1, arg2, arg3):
    """Function to do some evaluation.

    Args:
        arg1(optional): user input.
        arg2(optional): user input.
        arg3(optional): user input.

    Returns:
        bool: boolean value if inputs have the same data type.

    Examples:
        >>> exception_test(['apple'], 0, 'p')
        False
    """
    caught = False
    try:
        arg1[arg2].index(arg3)
    except (TypeError, KeyError, IndexError):
        caught = True

    return caught

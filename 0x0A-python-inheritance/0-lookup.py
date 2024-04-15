#!/usr/bin/python3
"""Defines object attribute lookup function."""


def lookup(obj):
    """Returns a list of an object available attributes."""
    return (dir(obj))

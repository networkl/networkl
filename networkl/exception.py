# -*- coding: utf-8 -*-
#    This code is part of the NetworkL package http://networkl.github.io
#    Copyright (C) 2015 by
#    Moreno Bonaventura <morenobonaventura@gmail.com>
#    This is Free Software - You can use and distribute it under
#    the terms of the GNU General Public License, version 3 or later.
"""
Exceptions
Base exceptions and errors for NetworkL.
"""
__author__ = """Moreno Bonaventura (morenobonaventura@gmail.com)"""


# root of all Exceptions
class NetworkLException(Exception):
    """Base class for exceptions in NetworkL."""

class NetworkLError(NetworkLException):
    """Exception for a serious error in NetworkL"""

class NetworkLAlgorithmError(NetworkLException):
    """Exception for unexpected termination of algorithms."""

class NetworkLNotImplemented(NetworkLException):
    """Exception raised by algorithms not implemented for a type of graph."""

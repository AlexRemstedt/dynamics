# encoding: utf-8
# Author: Alex Remstedt
"""
This module has some basic converting functions.
"""
import math
import numpy as np


# Functions
def rad_to_deg(theta):
    """
    transform radians to degrees

    :param theta: angle in radians
    :return: angle in degrees
    """
    return theta / math.pi * 180


def deg_to_rad(theta):
    """
    transform degrees to radians

    :param theta: angle in degrees
    :return: angle in radians
    """
    return theta / 180 * math.pi


def to_accent(coordinate, theta):
    """
    transpose coordinate

    :param coordinate: coordinate
    :param theta: angle in radians

    :type coordinate: np.ndarray

    :return: transposed coordinate
    """
    x = np.cos(theta) * coordinate[0] + np.sin(theta) * coordinate[1]
    y = np.sin(theta) * coordinate[0] + np.cos(theta) * coordinate[1]
    return np.array([x, y])


def from_accent(coordinate, theta):
    """
    transpose coordinate

    :param coordinate: coordinate
    :param theta: angle in radians

    :type coordinate: np.ndarray

    :return: transposed coordinate
    """
    x = np.arccos(theta) * coordinate[0] + np.arcsin(theta) * coordinate[1]
    y = np.arcsin(theta) * coordinate[0] + np.arccos(theta) * coordinate[1]
    return np.array([x, y])

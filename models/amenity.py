#!/usr/bin/python3
"""This module defines a class Amenity"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel
    Attributes:
        name (str): The amenity name."""
    name = ""

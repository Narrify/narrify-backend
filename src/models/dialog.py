"""
TODO
"""

from typing import List
from pydantic import BaseModel

from src.models.shared import Character


class DialogSettings(BaseModel):
    """
    TODO
    """

    number_of_scenes: int
    number_of_characters: int


class DialogRequest(BaseModel):
    """
    TODO
    """

    story: str
    settings: DialogSettings
    characters: List[Character]

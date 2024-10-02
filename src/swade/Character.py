from dataclasses import dataclass, field
from typing import Dict
from .DieType import DieType
from .Skill import Skill


@dataclass
class Character:
    """
    Character class represents a character in a role-playing game with various attributes and skills.

    Attributes:
        name (str): The name of the character.
        height (str): The height of the character.
        weight (str): The weight of the character.
        agility (DieType): The agility attribute of the character, default is DieType.d4.
        smarts (DieType): The smarts attribute of the character, default is DieType.d4.
        spirit (DieType): The spirit attribute of the character, default is DieType.d4.
        strength (DieType): The strength attribute of the character, default is DieType.d4.
        vigor (DieType): The vigor attribute of the character, default is DieType.d4.
        pace (int): The pace attribute of the character, default is 6.
        skills (dict[Skill]): A dictionary of skills the character possesses, default is an empty dictionary.

    Methods:
        __post_init__: Initializes additional attributes like toughness and parry after the object is created.
    """
    name: str
    height: str
    weight: str
    agility: DieType = DieType.d4
    smarts: DieType = DieType.d4
    spirit: DieType = DieType.d4
    strength: DieType = DieType.d4
    vigor: DieType = DieType.d4
    
    skills: Dict[Skill, DieType] = field(default_factory=dict)
    

    def __post_init__(self):
        self.toughness = int((self.vigor.value / 2) + 2)
        self.parry = 2  # Initialize parry with a default value or proper calculation

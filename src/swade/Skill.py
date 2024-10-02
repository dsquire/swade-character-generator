from dataclasses import dataclass
from DieType import DieType


@dataclass
class Skill:
    name: str
    linked_attribute: str
    base: DieType = DieType.d4
    modifier: int = 0    

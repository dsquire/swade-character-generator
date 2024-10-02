from enum import Enum


class DieType(Enum):
    d4 = 4
    d6 = 6
    d8 = 8
    d10 = 10
    d12 = 12

# Example usage
def roll_die(die_type: DieType):
    import random
    return random.randint(1, die_type.value)

# Example roll
print(roll_die(DieType.d6))

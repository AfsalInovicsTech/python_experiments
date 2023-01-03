
from enum import Enum

class PrimaryColors(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


print(f"PrimaryColors are: {PrimaryColors.RED.value}, {PrimaryColors.GREEN.value}, {PrimaryColors.BLUE.value}")


from enum import StrEnum, auto

class PrimaryColors(StrEnum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()


print(f"PrimaryColors are: {PrimaryColors.RED.value}, {PrimaryColors.GREEN.value}, {PrimaryColors.BLUE.value}")
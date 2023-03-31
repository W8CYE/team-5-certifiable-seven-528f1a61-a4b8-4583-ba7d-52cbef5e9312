from enum import Enum
from typing import Tuple, List
from levelup.position import Position


class Direction(Enum):
    NORTH = "n"
    SOUTH = "s"
    EAST = "e"
    WEST = "w"


class GameMap:
    starting_position: Position = Position(0, 0)
    size: Tuple[int, int] = (10, 10)
    position_count: int = 0
    positions: List[Position] = []

    def __init__(self):
        self.create_positions()

    def create_positions(self) -> None:
        self.positions = []
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                self.positions.append(Position(x, y))
        self.position_count = len(self.positions)
        

    def is_valid_position(self, position: Position) -> bool:
        pass

    def calculate_position(
        self, starting_position: Position, direction: Direction
    ) -> Position:
        pass

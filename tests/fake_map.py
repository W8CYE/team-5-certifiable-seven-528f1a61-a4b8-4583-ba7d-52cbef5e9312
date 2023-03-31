from levelup.position import Position
from levelup.map import GameMap, Direction


class FakeGameMap(GameMap):
    def __init__ (self):
        pass

    def calculate_position( self, starting_position: Position, direction: Direction) -> Position:
        return Position(111,222)
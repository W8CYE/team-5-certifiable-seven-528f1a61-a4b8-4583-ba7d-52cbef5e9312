from levelup.position import Position
from levelup.map import GameMap, Direction
from levelup.character import Character

DEFAULT_CHARACTER_NAME = "Character"

class FakeCharacter(Character):

    def __init__(self):
        self.position = Position(1,1)

    def move(self, dir: Direction):
        pass


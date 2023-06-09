import logging
from dataclasses import dataclass
from levelup.character import Character, DEFAULT_CHARACTER_NAME, InvalidMoveException
from levelup.map import Direction, GameMap
from levelup.position import Position

@dataclass
class GameStatus:
    move_count: int = 0
    running: bool = False
    character: Character = Character(DEFAULT_CHARACTER_NAME)
    current_position: Position = None
    # current_position: Position = Position(1,1)


    def __str__(self):
        return f"Moved {self.move_count} times, currently on position {self.current_position}"


class CharacterNotFoundException(Exception):
    pass


class GameController:
    status: GameStatus
    character: Character

    def __init__(self):
        self.status = GameStatus()
        self.character = Character(DEFAULT_CHARACTER_NAME)
        self.map = GameMap()
        # self.status.current_position = self.map.starting_position

    def start_game(self):
        if hasattr(self, "character"):
            self.character.enter_map(self.map)
            self.status.current_position = self.character.position
            self.set_character_position(self.map.starting_position)
        else:
            raise CharacterNotFoundException("Character not found")

    def create_character(self, character_name: str) -> None:
        self.character = Character(character_name)

    def move(self, direction: Direction) -> None:
        self.character.move(direction)
        self.status.move_count += 1

    def set_character_position(self, position: Position):
        self.character.position = position

    def get_total_positions(self):
        return self.map.position_count

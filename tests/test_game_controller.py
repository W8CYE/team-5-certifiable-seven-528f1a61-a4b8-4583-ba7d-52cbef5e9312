from unittest import TestCase
from unittest.mock import MagicMock, create_autospec
from levelup.controller import GameController, CharacterNotFoundException
from levelup.character import DEFAULT_CHARACTER_NAME, InvalidMoveException, Character
from levelup.map import Direction
from levelup.position import Position


class TestGameController(TestCase):
    def test_init(self):
        testobj = GameController()
        self.assertEqual(testobj.status.move_count, 0)
        self.assertEqual(
            testobj.status.current_position,
            None,
        )

    def test_create_default_chararacter(self):
        testobj = GameController()
        testobj.create_character("")
        self.assertEqual(DEFAULT_CHARACTER_NAME,testobj.character.name)

    def test_create_character(self):
        testobj = GameController()
        testobj.create_character("Bob")
        self.assertEqual("Bob", testobj.character.name)

    def test_start_game(self):
        testobj = GameController()
        testobj.start_game()
        self.assertEqual(Position(0,0),testobj.character.position)

        #self.assertNotEqual(testobj.status.current_position,None)

    def test_set_character_position(self):
        testobj = GameController()
        testobj.set_character_position(Position(15,15))
        self.assertEqual(Position(15,15),testobj.character.position)

    def test_get_total_positions(self):
        #testobj = GameController()
        #testobj.get_total_positions()
        #self.assertEqual(10, testobj.map.position_count)
        pass




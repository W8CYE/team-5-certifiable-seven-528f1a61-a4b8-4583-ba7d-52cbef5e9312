from unittest import TestCase
from levelup.character import Character, InvalidMoveException
from levelup.map import GameMap, Direction
from fake_map import FakeGameMap
from levelup.position import Position


class TestCharacter(TestCase):
    def test_init(self):
        expected_name = "arbitrary"
        testobj = Character(expected_name)
        self.assertEqual(testobj.name, expected_name)
        expected_position = None
        self.assertEqual(testobj.position, expected_position)

    def test_enter_map(self):
        expected_map = FakeGameMap()
        testobj = Character(None)
        testobj.enter_map(expected_map)
        self.assertEqual(testobj.map, expected_map)
        
    def test_move(self):
        expected_map = FakeGameMap()
        testobj = Character(None)
        testobj.enter_map(expected_map)
        testobj.position = Position(33,33)
        testobj.move(Direction.NORTH)
        self.assertEqual(str(testobj.position), str(Position(111,222)))

    def test_initial_position(self):
        expected_map = FakeGameMap()
        testobj = Character(None)
        testobj.enter_map(expected_map)
        self.assertEqual(str(testobj.position), str(Position(4,4)))


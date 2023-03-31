from unittest import TestCase
from levelup.map import GameMap
from levelup.position import Position

class TestMap(TestCase):
    def test_init(self):
        testobj = GameMap()
        self.assertEqual(
            testobj.position_count,
            100,
        )

    def test_is_valid_position_should_return_true_for_valid_position(self):
        testobj = GameMap()
        result=testobj.is_valid_position(Position(5,2))
        self.assertTrue(result)

    
    def test_is_valid_position_should_return_false_for_invalid_position(self):
        testobj = GameMap()
        result=testobj.is_valid_position(Position(5,25))
        self.assertFalse(result)    
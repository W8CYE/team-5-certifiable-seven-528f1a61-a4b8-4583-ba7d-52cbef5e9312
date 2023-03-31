from unittest import TestCase
from levelup.map import GameMap, Direction
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

    def test_calculate_position_north(self):
        testobj = GameMap()
        return_position: Position = None
        expected_position: Position = Position(4,3)
        input_position: Position =Position(4,2)
        input_direction: Direction =Direction.NORTH
        return_position= testobj.calculate_position(input_position,input_direction)
        self.assertEqual(return_position.coordinates, expected_position.coordinates)

    
    def test_calculate_position_south(self):
        testobj = GameMap()
        return_position: Position = None
        expected_position: Position = Position(4,1)
        input_position: Position =Position(4,2)
        input_direction: Direction =Direction.SOUTH
        return_position= testobj.calculate_position(input_position,input_direction)
        self.assertEqual(return_position.coordinates, expected_position.coordinates)

    
    def test_calculate_position_east(self):
        testobj = GameMap()
        return_position: Position = None
        expected_position: Position = Position(5,2)
        input_position: Position =Position(4,2)
        input_direction: Direction =Direction.EAST
        return_position= testobj.calculate_position(input_position,input_direction)
        self.assertEqual(return_position.coordinates, expected_position.coordinates)
    

    def test_calculate_position_west(self):
        testobj = GameMap()
        return_position: Position = None
        expected_position: Position = Position(3,2)
        input_position: Position =Position(4,2)
        input_direction: Direction =Direction.WEST
        return_position= testobj.calculate_position(input_position,input_direction)
        self.assertEqual(return_position.coordinates, expected_position.coordinates)
from unittest import TestCase
from levelup.map import GameMap


class TestMap(TestCase):
    def test_init(self):
        testobj = GameMap()
        self.assertEqual(
            testobj.position_count,
            100,
        )

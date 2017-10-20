#!/usr/bin/env python

import unittest
from SeekBot import SeekBot

class TestSeekBot(unittest.TestCase):

    botty = SeekBot()

    def setUp(self):
        pass

    def test_place(self):
        self.botty.place('NORTH',0,0)
        self.assertEqual(self.botty.direction,'NORTH')
        self.assertEqual(self.botty.xaxis,0)
        self.assertEqual(self.botty.yaxis,0)
        self.botty.place('WEST',6,6)
        self.assertEqual(self.botty.direction,'WEST')
        self.assertEqual(self.botty.xaxis,4)
        self.assertEqual(self.botty.yaxis,4)
        self.botty.place('EAST',-1,-1)
        self.assertEqual(self.botty.direction,'EAST')
        self.assertEqual(self.botty.xaxis,0)
        self.assertEqual(self.botty.yaxis,0)

    def test_move(self):
        self.botty.move()
        self.assertEqual(self.botty.direction,'NORTH')
        self.assertEqual(self.botty.xaxis,0)
        self.assertEqual(self.botty.yaxis,1)

    def test_left(self):
        self.botty.direction = 'NORTH'
        self.botty.left()
        self.assertEqual(self.botty.direction,'WEST')
        self.botty.left()
        self.assertEqual(self.botty.direction,'SOUTH')
        self.botty.left()
        self.assertEqual(self.botty.direction,'EAST')
        self.botty.left()
        self.assertEqual(self.botty.direction,'NORTH')
        self.assertEqual(self.botty.xaxis,0)
        self.assertEqual(self.botty.yaxis,0)

    def test_right(self):
        self.botty.direction = 'NORTH'
        self.botty.right()
        self.assertEqual(self.botty.direction,'EAST')
        self.botty.right()
        self.assertEqual(self.botty.direction,'SOUTH')
        self.botty.right()
        self.assertEqual(self.botty.direction,'WEST')
        self.botty.right()
        self.assertEqual(self.botty.direction,'NORTH')
        self.assertEqual(self.botty.xaxis,0)
        self.assertEqual(self.botty.yaxis,0)

if __name__ == '__main__':
    unittest.main()

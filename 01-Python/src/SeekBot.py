#!/usr/bin/env python

class SeekBot(object):
    direction='NORTH'
    xaxis=0
    yaxis=0
    """docstring for SeekBot."""
    def __init__(self):
        super(SeekBot, self).__init__()

    def place(self, direction, xaxis, yaxis):
        self.direction = direction
        self.xaxis = xaxis
        self.yaxis = yaxis
        self.check_position()

    def left(self):
        if self.direction == 'NORTH':
            self.direction = 'WEST'
        elif self.direction == 'WEST':
            self.direction = 'SOUTH'
        elif self.direction == 'SOUTH':
            self.direction = 'EAST'
        else:
            self.direction = 'NORTH'

    def right(self):
        if self.direction == 'NORTH':
            self.direction = 'EAST'
        elif self.direction == 'EAST':
            self.direction = 'SOUTH'
        elif self.direction == 'SOUTH':
            self.direction = 'WEST'
        else:
            self.direction = 'NORTH'

    def move(self):
        if self.direction == 'NORTH':
            self.yaxis = self.yaxis + 1
        if self.direction == 'SOUTH':
            self.yaxis = self.yaxis - 1
        if self.direction == 'EAST':
            self.xaxis = self.xaxis + 1
        if self.direction == 'WEST':
            self.xaxis = self.xaxis - 1
        self.check_position()

    def check_position(self):
        if self.xaxis < 0:
            self.xaxis = 0
        if self.xaxis > 4:
            self.xaxis = 4
        if self.yaxis < 0:
            self.yaxis = 0
        if self.yaxis > 4:
            self.yaxis = 4

    def report(self):
        print(self.xaxis,self.yaxis,self.direction)

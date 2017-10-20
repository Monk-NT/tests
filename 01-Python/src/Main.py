#!/usr/bin/env python

import sys
from SeekBot import SeekBot

def main(input):
    try:
        extract_commands(input)
    except AssertionError as e:
        print(e.args)


def extract_commands(input_list):
    botty = SeekBot()
    if len(input_list) >= 2 :
        if input_list[0] == 'PLACE':
            place_data = input_list[1].split(',')
            if (len(place_data) < 3):
                raise AssertionError("There is not enough data to place the robot!")
            xaxis=int(place_data[0])
            yaxis=int(place_data[1])
            if (0 <= xaxis <= 4) and (0 <= yaxis <= 4):
                botty.place(place_data[2],xaxis,yaxis)
            else:
                raise AssertionError("Placing bot outside of bounds")
        else:
            raise AssertionError("Doesn't start with PLACE")
    else:
        raise AssertionError("Command input should begin with at least PLACE x,y,direction")
    if len(input_list) > 2:
        for cmd in input_list[2:]:
            print cmd
            if cmd == 'REPORT':
                botty.report()
            elif cmd == 'MOVE':
                botty.move()
            elif cmd == 'LEFT':
                botty.left()
            elif cmd == 'RIGHT':
                botty.rigth()
            else:
                raise AssertionError("Unknown command used. Aborting")

if __name__ == '__main__':
    main(sys.argv[1:]);

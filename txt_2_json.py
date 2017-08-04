#!/usr/bin/env python2

for line in open('corners.txt'):
    tokens = line.split(' ', 4)
    name, face1, face2, _dash, moves = tokens
    name = name[:-1]
    move = moves.split()
    print name, face1, face2,  move

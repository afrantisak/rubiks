#!/usr/bin/env python2
import json
import collections

for line in open('corners.txt'):
    tokens = line.split(' ', 4)
    name, face1, face2, _dash, moves = tokens
    name = name[:-1]
    move = moves.split()
    json_obj = collections.OrderedDict([
        ('name', name),
        ('face1', face1),
        ('face2', face2),
        ('move', move)
    ])
    print json.dumps(json_obj)

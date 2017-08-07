#!/usr/bin/env python2
import json
import operator
import collections

moves = []
for json_str in open('corners.json'):
    json_obj = json.loads(json_str, object_pairs_hook=collections.OrderedDict)
    moves.append(json_obj)

for move in sorted(moves, key=lambda move: move['move']):
    name = move['name']
    move_str = ' '.join(move['move'])
    img = '<img src="file:///home/franta/dev/rubiks/{name}.png"/>'.format(**locals())
    print '<html>'
    print '<body>'
    print img, json.dumps(move_str), '<BR>'
    print '</body>'
    print '</html>'

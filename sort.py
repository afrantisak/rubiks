#!/usr/bin/env python2
import sys
import json
import util
import html
import html_format
import operator
import collections


def load_moves(filename):
    moves = []
    for json_str in open(filename):
        json_obj = json.loads(json_str, object_pairs_hook=collections.OrderedDict)
        moves.append(json_obj)
    return moves


def main():
    moves = load_moves('corners.json')
    html = html_format.moves_2_html(moves)
    print html


if __name__ == '__main__':
    sys.exit(main())

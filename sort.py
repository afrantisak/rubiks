#!/usr/bin/env python2
import sys
import json
import html
import operator
import collections


def flip_turn(turn):
    flip = {
        'F':  'Fi',
        'Fi': 'F',
        'R':  'Ri',
        'Ri': 'R',
        'L':  'Li',
        'Li': 'L',
        'U':  'Ui',
        'Ui': 'U',
        'D':  'Di',
        'Di': 'D',
        'B':  'Bi',
        'Bi': 'B',
    }
    if turn in flip:
        return flip[str(turn)]
    return turn


def reverse_move(move):
    move = reversed(move)
    move = [flip_turn(turn) for turn in move]
    return move


def move_html(move):
    name = move['name']
    html = ''
    move_str = turn_table(move['move'])
    back_str = turn_table(reverse_move(move['move']))
    img = '<img src="http://127.0.0.1:8000/{name}.png"/>'.format(**locals())
    html += '<table><tr>'
    html += '<td>' + name + '</td>'
    html += '<td align="right" style=\'width: 300px; \'>' + back_str + '</td>'
    html += '<td>' + img + '</td>'
    html += '<td style=\'width: 300px\'>' + move_str + '</td>'
    html += '</tr>'
    html += '</table>'
    return html


def turn_html_text(turn):
    if len(turn) > 1:
        if turn[1] == '2':
            turn = turn[0] + '<sup>' + turn[1] + '</sup>'
        if turn[1] == 'i':
            turn = turn[0] + '<sub>' + turn[1] + '</sub>'
    return turn


def turn_table(move):
    move_cell_props = {
        'align': 'center',
        'valign': 'baseline',
        'style': {
            'width': '18px',
            'border': '1px solid gray',
            'padding': '5px',
            'border-collapse': 'collapse'
        }
    }
    move_row_props = {
        'style': {
            'border-spacing': '0px',
            'border-collapse': 'collapse',
        }
    }
    table_props = {
        'style': {
            'border-spacing': '0px',
            'border-collapse': 'collapse',
        }
    }
    move_cell_attributes = html.attributes_text(move_cell_props)
    move_row_attributes = html.attributes_text(move_row_props)
    table_attributes = html.attributes_text(table_props)
    html_text = '<table {table_attributes}>'.format(**locals())
    html_text += '<tr {move_row_attributes}>'.format(**locals())
    for turn in move:
        html_text += '<td {move_cell_attributes}>'.format(**locals())
        html_text += turn_html_text(turn)
        html_text += '</td>'
    html_text += '</tr>'
    html_text += '</table>'
    return html_text


def load_moves(filename):
    moves = []
    for json_str in open(filename):
        json_obj = json.loads(json_str, object_pairs_hook=collections.OrderedDict)
        moves.append(json_obj)
    return moves


def moves_html(moves):
    html = ''
    html += '<html>'
    html += '<body>'
    html += '<font face="Mono" size="3">'
    html += '<center>'
    html += '<BR>'
    html += '<table style="border: 1px solid black; padding=0px; border-collapse: collapse">'
    for index, move in enumerate(sorted(moves, key=lambda move: move['move'])):
        html += '<tr><td>'
        html += move_html(move)
        html += '</td></tr>'
        html += '</table>'
        if index % 10 == 9:
            html += '<BR>'* 3
        html += '<table style="border: 1px solid black">'
    html += '</table>'
    html += '</center>'
    html += '</font>'
    html += '</body>'
    html += '</html>'
    return html


def main():
    moves = load_moves('corners.json')
    html = moves_html(moves)
    print html


if __name__ == '__main__':
    sys.exit(main())

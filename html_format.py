import html
import util

def move_2_html(move):
    name = move['name']
    html = ''
    move_str = turns_2_table(move['move'])
    back_str = turns_2_table(util.reverse_move(move['move']))
    img = '<img src="http://127.0.0.1:8000/{name}.png"/>'.format(**locals())
    html += '<table><tr>'
    html += '<td>' + name + '</td>'
    html += '<td align="right" style=\'width: 300px; \'>' + back_str + '</td>'
    html += '<td>' + img + '</td>'
    html += '<td style=\'width: 300px\'>' + move_str + '</td>'
    html += '</tr>'
    html += '</table>'
    return html


def turn_2_html(turn):
    if len(turn) > 1:
        if turn[1] == '2':
            turn = turn[0] + '<sup>' + turn[1] + '</sup>'
        if turn[1] == 'i':
            turn = turn[0] + '<sub>' + turn[1] + '</sub>'
    return turn


def turns_2_table(move):
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
        html_text += turn_2_html(turn)
        html_text += '</td>'
    html_text += '</tr>'
    html_text += '</table>'
    return html_text


def moves_2_html(moves):
    html = ''
    html += '<html>'
    html += '<body>'
    html += '<font face="Mono" size="3">'
    html += '<center>'
    html += '<BR>'
    html += '<table style="border: 1px solid black; padding=0px; border-collapse: collapse">'
    for index, move in enumerate(sorted(moves, key=lambda move: move['move'])):
        html += '<tr><td>'
        html += move_2_html(move)
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

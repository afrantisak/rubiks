import html
import util

def turn_html(turn):
    if len(turn) > 1:
        if turn[1] == '2':
            turn = turn[0] + '<sup>' + turn[1] + '</sup>'
        if turn[1] == 'i':
            turn = turn[0] + '<sub>' + turn[1] + '</sub>'
    return turn


def turns_html(move):
    props = {
        'cell': {
            'align': 'center',
            'valign': 'baseline',
            'style': {
                'width': '18px',
                'border': '1px solid gray',
                'padding': '5px',
                'border-collapse': 'collapse'
            }
        },
        'row': {
            'style': {
                'border-spacing': '0px',
                'border-collapse': 'collapse',
            }
        },
        'table': {
            'style': {
                'border-spacing': '0px',
                'border-collapse': 'collapse',
            }
        },
    }
    return html.table_single_row(move, turn_html, props)


def algorithm_html(move):
    name = move['name']
    html = ''
    move_str = turns_html(move['move'])
    back_str = turns_html(util.reverse_move(move['move']))
    img = '<img src="http://127.0.0.1:8000/{name}.png"/>'.format(**locals())
    html += '<table><tr>'
    # html += '<td>' + name + '</td>'
    # html += '<td align="right" style=\'width: 170px; \'>' + back_str + '</td>'
    html += '<td>' + img + '</td>'
    html += '<td style=\'width: 170px\'>' + move_str + '</td>'
    html += '</tr>'
    html += '</table>'
    return html


def page_html(moves):
    html = ''
    html += '<html>'
    html += '<body>'
    html += '<font face="Mono" size="3">'
    html += '<center>'
    html += '<BR>'
    html += '<table style="border: 1px solid black; padding=0px; border-collapse: collapse">'
    for index, move in enumerate(sorted(moves, key=lambda move: move['move'])):
        html += '<tr><td>'
        html += algorithm_html(move)
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

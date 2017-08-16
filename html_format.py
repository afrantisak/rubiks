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
    move = [move]
    return html.table(move, turn_html, props)


def algorithm_html(move):
    name = move['name']
    html_text = ''
    move_str = turns_html(move['move'])
    back_str = turns_html(util.reverse_move(move['move']))
    img = html.img_cropped('http://127.0.0.1:8000/{name}.png'.format(**locals()), '70px', '63px', '68px', '-6px', '-9px')
    html_text += '<table><tr>'
    html_text += '<td>' + name + '</td>'
    html_text += '<td align="right" style=\'width: 170px; \'>' + back_str + '</td>'
    html_text += '<td>' + img + '</td>'
    html_text += '<td style=\'width: 170px\'>' + move_str + '</td>'
    html_text += '</tr>'
    html_text += '</table>'
    return html_text


def page_html(moves):
    html_text = ''
    html_text += '<html>'
    html_text += '<body>'
    html_text += '<font face="Mono" size="3">'
    html_text += '<center>'
    html_text += '<BR>'
    props = {
        'cell': {
            'align': 'center',
            'valign': 'baseline',
            'style': {
                'border': '1px solid black',
                'padding': '1px',
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
    moves_data = sorted(moves, key=lambda move: move['move'])
    moves_data = [[move] for move in moves_data]
    html_text += html.table(moves_data, algorithm_html, props)
    html_text += '</center>'
    html_text += '</font>'
    html_text += '</body>'
    html_text += '</html>'
    return html_text

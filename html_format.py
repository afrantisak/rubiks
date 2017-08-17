import html
import util
import collections


MOVE_TABLE_ATTRIBUTES = {
    'cell': {
        'align': 'center',
        'valign': 'baseline',
        'style': {
            'border': '1px solid gray',
            'padding': '2px',
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


TURN_TABLE_ATTRIBUTES = {
    'cell': {
        'align': 'left',
        'valign': 'baseline',
        'style': {
            'width': '18px',
            'height': '20px',
            'border': '0px dotted gray',
            'padding': '3px',
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


def turn_html(turn):
    sup_attributes = html.attributes_text({
        'vertical-align': 'baseline',
        'position': 'relative',
        'top': '-0.4em',
    })
    sub_attributes = html.attributes_text({
        'vertical-align': 'baseline',
        'position': 'relative',
        'top': '0.4em',
    })
    if len(turn) > 1:
        if turn[1] == '2':
            turn = turn[0] + '<sup {sup_attributes}>'.format(**locals()) + turn[1] + '</sup>'
        if turn[1] == 'i':
            turn = turn[0] + '<sub {sub_attributes}>'.format(**locals()) + turn[1] + '</sub>'
    return turn


def turns_html(move):
    return html.table([move], turn_html, TURN_TABLE_ATTRIBUTES)


def algorithm_html(move):
    name = move['name']
    html_text = ''
    move_str = turns_html(move['move'])
    back_str = turns_html(util.reverse_move(move['move']))
    img = html.img_cropped('http://127.0.0.1:8000/{name}.png'.format(**locals()), '70px', '63px', '68px', '-6px', '-9px')
    html_text += '<table><tr>'
    # html_text += '<td>' + name + '</td>'
    # html_text += '<td align="right" style=\'width: 170px; \'>' + back_str + '</td>'
    html_text += '<td>' + img + '</td>'
    html_text += '<td style=\'width: 150px\'>' + move_str + '</td>'
    html_text += '</tr>'
    html_text += '</table>'
    return html_text


def move_table(moves):
    moves_data = [[move] for move in moves]
    html_text = html.table(moves_data, algorithm_html, MOVE_TABLE_ATTRIBUTES)
    return html_text


def page_html(moves):
    html_text = ''
    html_text += '<html>'
    html_text += '<body>'
    html_text += '<font face="Mono" size="3">'
    html_text += '<center>'
    html_text += '<BR>'
    moves_data = sorted(moves, key=lambda move: move['move'])
    moves_by_first = collections.OrderedDict()
    for move in moves_data:
        key = move['move'][0]
        if key not in moves_by_first:
            moves_by_first[key] = []
        moves_by_first[key] += [move]
    for first, move_group in moves_by_first.iteritems():
        html_text += move_table(move_group)
        html_text += '<BR>'
    html_text += '</center>'
    html_text += '</font>'
    html_text += '</body>'
    html_text += '</html>'
    return html_text

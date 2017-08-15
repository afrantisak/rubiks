def key_value_pair(key, value):
    return ' {key}="{value}"'.format(**locals())


def style_pair(key, styles):
    style = ' {key}="'.format(**locals())
    for key, value in styles.iteritems():
        style += ' {key}: {value};'.format(**locals())
    style += '"'
    return style


def attributes_text(props):
    attributes = ''
    for key, value in props.iteritems():
        if key == 'style':
            attributes += style_pair(key, value)
        else:
            attributes += key_value_pair(key, value)
    return attributes


def table_single_row(table_data, cell_func, props):
    table_attributes = attributes_text(props['table'])
    row_attributes = attributes_text(props['row'])
    cell_attributes = attributes_text(props['cell'])
    html = '<table {table_attributes}>'.format(**locals())
    html += '<tr {row_attributes}>'.format(**locals())
    for cell_data in table_data:
        html += '<td {cell_attributes}>'.format(**locals())
        html += cell_func(cell_data)
        html += '</td>'
    html += '</tr>'
    html += '</table>'
    return html

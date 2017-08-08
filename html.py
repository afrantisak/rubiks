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

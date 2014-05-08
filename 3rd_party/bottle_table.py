from bottle import route, run


def table(n):
    return [[i * j for j in range(1, n + 1)] for i in range(1, n + 1)]

def html_renderer(table):
    l = ['<table border="1">\n']
    for row in table:
        l.append('<tr>')
        for i in row:
            l.append('<td>{}</td>'.format(i))
        l.append('</tr>\n')
    l.append('</table>\n')
    return ''.join(l)


@route('/<n>')
def index(n):
    return html_renderer(table(int(n)))

run(host='localhost', port=8080)
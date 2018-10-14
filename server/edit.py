
_tempate = ''
with open('web_assets/edit.tp','r') as f:
    _template = f.read()
_row = ''
with open('web_assets/edit_row.tp','r') as f:
    _row = f.read()
    
def build(data):
    table = ''
    for r in data + ['','','']:
        table += _row
            .replace('{{{DIFF}}}', r[2])
            .replace('{{{RECV}}}', r[1])
            .replace('{{{SEND}}}', r[0])
    return _template.replace('{{{TABLE}}}', table)

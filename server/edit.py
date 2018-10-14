
_tempate = ''
with open('web_assets/edit.tp','r') as f:
    _template = f.read()
_row = ''
with open('web_assets/edit_row.tp','r') as f:
    _row = f.read()
    
def build(user, data):
    table = ''
    for r in data.items():
        table += _row \
            .replace('{{{DIFF}}}', r[1]) \
            .replace('{{{SEND}}}', r[0])
    table += _row \
            .replace('{{{DIFF}}}', '') \
            .replace('{{{SEND}}}', '')
    return _template \
        .replace('{{{TABLE}}}', table) \
        .replace('{{{USER}}}', user)

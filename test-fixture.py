from pathlib import Path
html = Path('index.html').read_text()
assert html.startswith('<!doctype html>')
for expected in ['<h1>', 'Demo Item', '<td>2</td>', '<td>7</td>', '<td>14</td>']:
    assert expected in html, expected
assert '<script' not in html
assert '<h1>Seed inventory</h1>' in html, 'heading should be "Seed inventory"'
assert 'background-color: lightblue' in html, 'table header should have light blue background'
print('fixture checks passed')

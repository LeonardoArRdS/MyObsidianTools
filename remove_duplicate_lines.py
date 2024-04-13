import clipboard
from util import keyboard_read_lines

'''
Input:
[[C]]
[[A]]
[[B]]
[[A]]

Output:
[[A]]
[[B]]
[[C]]
'''

order = True

lines = keyboard_read_lines()
lines = list(set(lines))

if order:
    lines.sort()

clipboard.copy("\n".join(lines))
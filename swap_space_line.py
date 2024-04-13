import clipboard
from util import keyboard_read_lines

linhas = keyboard_read_lines()

sep = " [["
if len(linhas) == 1:
    texto = "\n[[".join(linhas[0].split(" [["))
else:
    texto = " ".join(linhas)
clipboard.copy(texto)
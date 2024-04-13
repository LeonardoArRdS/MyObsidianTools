
def keyboard_read_lines():
    linhas = []
    while True:
        linha = input()
        if linha == "" or linha == "\n": break
        linhas.append(linha)
    return linhas
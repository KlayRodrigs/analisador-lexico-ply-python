from parser import parser, gerar_html_css
from tokens import lexer

def main():
    print("Digite seu código. Para finalizar, digite uma linha vazia.\n")
    linhas = []
    while True:
        linha = input('> ')
        if linha.strip() == '':
            break
        linhas.append(linha)

    codigo = '\n'.join(linhas)
    parser.parse(codigo, lexer=lexer)

    gerar_html_css()


if __name__ == '__main__':
    main()

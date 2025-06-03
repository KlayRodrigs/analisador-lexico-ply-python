import ply.lex as lex

tokens = [
    'NUMERO',
    'STRING',
]

reservadas = {
    'criar': 'CRIAR',
    'tela': 'TELA',
    'cabecalho': 'CABECALHO',
    'texto': 'TEXTO',
    'botao': 'BOTAO',
    'rodape': 'RODAPE',
    'imagem': 'IMAGEM',
    'centralizado': 'CENTRALIZADO',
    'grande': 'GRANDE',
    'largura': 'LARGURA',
    'altura': 'ALTURA',
    'display': 'DISPLAY',
    'grid': 'GRID',
    'flex': 'FLEX',
    'espaco': 'ESPACO',
}

tokens += list(reservadas.values())


t_ignore = ' \t' 


def t_STRING(t):
    r'\".*?\"'
    t.value = t.value.strip('"')
    return t


def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_palavras(t):
    r'[a-zA-ZçÇãõéá]+'
    t.type = reservadas.get(t.value.lower(), 'STRING')
    return t


def t_error(t):
    print(f'Caractere inválido: {t.value[0]}')
    t.lexer.skip(1)


lexer = lex.lex()

if __name__ == '__main__':
    data = '''
    criar tela altura 600 largura 800
    cabecalho centralizado grande "Minha Pagina"
    texto centralizado "Bem vindo ao site"
    botao "Clique aqui"
    rodape "Desenvolvido por Fulano"
    '''
    lexer.input(data)
    for tok in lexer:
        print(tok)

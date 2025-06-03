import ply.yacc as yacc
from tokens import tokens, lexer

html_elements = []
tela_config = {'largura': 800, 'altura': 600, 'display': 'block'}  # display padrão

def p_program(p):
    '''program : comandos'''
    p[0] = p[1]


def p_comandos_multiplos(p):
    '''comandos : comandos comando'''
    p[0] = p[1] + [p[2]]


def p_comandos_unico(p):
    '''comandos : comando'''
    p[0] = [p[1]]


def p_comando_criar_tela(p):
    '''comando : CRIAR TELA ALTURA NUMERO LARGURA NUMERO'''
    tela_config['altura'] = p[4]
    tela_config['largura'] = p[6]
    print(f'Tela criada {p[6]}x{p[4]}')

def p_comando_display(p):
    '''comando : DISPLAY GRID
               | DISPLAY FLEX'''
    tela_config['display'] = p[2].lower()
    print(f"Display definido como {p[2].lower()}")


def p_comando_cabecalho(p):
    '''comando : CABECALHO CENTRALIZADO GRANDE STRING'''
    html_elements.append(f'<h1 style="text-align:center;">{p[4]}</h1>')


def p_comando_texto(p):
    '''comando : TEXTO CENTRALIZADO STRING'''
    html_elements.append(f'<p style="text-align:center;">{p[3]}</p>')


def p_comando_botao(p):
    '''comando : BOTAO STRING'''
    html_elements.append(f'<button>{p[2]}</button>')


def p_comando_botao_centralizado(p):
    '''comando : BOTAO CENTRALIZADO STRING'''
    html_elements.append(f'<div style="text-align:center;"><button>{p[3]}</button></div>')

def p_comando_espaco(p):
    '''comando : ESPACO'''
    html_elements.append('<br>')


def p_comando_rodape(p):
    '''comando : RODAPE STRING'''
    html_elements.append(f'<footer>{p[2]}</footer>')


def p_comando_imagem(p):
    '''comando : IMAGEM STRING ALTURA NUMERO LARGURA NUMERO'''
    html_elements.append(
        f'<img src="{p[2]}" height="{p[4]}" width="{p[6]}"/>'
    )

def p_comando_imagem_centralizada(p):
    '''comando : IMAGEM STRING CENTRALIZADO ALTURA NUMERO LARGURA NUMERO'''
    html_elements.append(
        f'<div style="text-align:center;"><img src="{p[2]}" height="{p[5]}" width="{p[7]}" style="display:inline-block;"/></div>'
    )


def p_error(p):
    if p:
        print(f"Erro de sintaxe em '{p.value}'")
    else:
        print("Erro de sintaxe no final do arquivo")


parser = yacc.yacc()


def gerar_html_css():
    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Minha Página</title>
<style>
body {{
    width: {tela_config['largura']}px;
    height: {tela_config['altura']}px;
    margin: 0 auto;
    background-color: #f0f0f0;
    font-family: Arial, sans-serif;
    display: {tela_config['display']};
    {'justify-content: center; align-items: center;' if tela_config['display'] in ['flex', 'grid'] else ''}
}}
button {{
    padding: 10px 20px;
    background-color: #007BFF;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}}
footer {{
    text-align: center;
    margin-top: 20px;
    color: #666;
}}
</style>
</head>
<body>
{''.join(html_elements)}
</body>
</html>"""
    with open('saida.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('Arquivo HTML gerado: saida.html')

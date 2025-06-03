# 🧩 Analisador Léxico com PLY

Este projeto implementa um analisador léxico (lexer) utilizando a biblioteca PLY em Python, para uma linguagem de comandos simples voltada à criação de páginas visuais.

## 🔧 1. Definindo os Tokens

O analisador reconhece comandos específicos para construção de páginas, como criação de telas, cabecalhos, textos, botões, imagens e rodapés, além de atributos de formatação.

### 📜 Exemplos de Comandos da Linguagem

```
criar tela altura 600 largura 800
cabecalho centralizado grande "Minha Página"
espaco
texto centralizado "Bem vindo ao site"
botao centralizado "Clique aqui"
imagem "foto.jpeg" centralizado altura 300 largura 200
espaco
rodape "Rodape simples"
```

#### Exemplo Completo para Teste

Copie e cole o exemplo abaixo para testar todos os tokens e comandos disponíveis na linguagem:

```
criar tela altura 600 largura 800

display grid

cabecalho centralizado grande "Minha Pagina"
cabecalho "Cabecalho a esquerda"
cabecalho centralizado "Cabecalho centralizado menor"
espaco

texto centralizado "Texto centralizado"
texto centralizado "Texto centralizado 2"
espaco

botao "Botao simples"
espaco
botao centralizado "Botao centralizado"
espaco

imagem "foto.jpeg" altura 150 largura 150
imagem "foto.jpeg" centralizado altura 200 largura 300
espaco

rodape "Rodape simples"
rodape "Outro rodape"
```

Esse exemplo cobre todos os tokens e palavras-chave da linguagem: CRIAR, TELA, ALTURA, LARGURA, DISPLAY, GRID, FLEX, CABECALHO, CENTRALIZADO, GRANDE, TEXTO, BOTAO, IMAGEM, RODAPE, ESPACO, além de diferentes variações de uso.


### 🔤 Tokens Necessários

- **Palavras-chave:**  
  `CRIAR`, `TELA`, `CABECALHO`, `TEXTO`, `BOTAO`, `IMAGEM`, `RODAPE`, `CENTRALIZADO`, `GRANDE`, `LARGURA`, `ALTURA`, `DISPLAY`, `GRID`, `FLEX`, `ESPACO`
- **Números:**  
  Utilizados para dimensões (ex: `800`, `600`, `300`, `200`)
- **Strings:**  
  Para textos e nomes de arquivos (ex: `"Minha Pagina"`, `"foto.jpeg"`)

#### O que cada palavra-chave faz?
- **CRIAR TELA ALTURA N LARGURA N**: Define o tamanho da página.
- **DISPLAY GRID/FLEX**: Define o tipo de layout principal (grid ou flex).
- **CABECALHO [CENTRALIZADO] [GRANDE] "texto"**: Adiciona um cabeçalho (h1), podendo ser centralizado e/ou grande.
- **TEXTO [CENTRALIZADO] "texto"**: Adiciona um parágrafo, podendo ser centralizado.
- **BOTAO [CENTRALIZADO] "texto"**: Adiciona um botão, podendo ser centralizado.
- **IMAGEM "arquivo" [CENTRALIZADO] ALTURA N LARGURA N**: Adiciona uma imagem, podendo ser centralizada, com altura e largura.
- **RODAPE "texto"**: Adiciona um rodapé.
- **ESPACO**: Adiciona uma quebra de linha (`<br>`).

### ℹ️ Observações e Limitações
- Use sempre as palavras-chave SEM acento.
- O comando `display` aceita apenas `grid` ou `flex`.
- O comando `imagem` exige altura e largura, e pode ser centralizado.
- O comando `cabecalho` pode ser simples, centralizado, grande, ou ambas.
- O arquivo `saida.html` será sobrescrito a cada execução.

### ❓ Dúvidas Frequentes
- **Por que minha palavra-chave não funciona?**
  - Verifique se está sem acento e na ordem correta.
- **Como vejo o resultado?**
  - Abra o arquivo `saida.html` no navegador após rodar o `main.py` ou baixe a extensão `Live Server` no VSCode e abra o arquivo `saida.html` com ele.
- **Posso mudar as cores ou o layout?**
  - Edite o CSS gerado em `parser.py` conforme desejar.

  `x` (utilizado para separar dimensões, como em `800x600`)

## 🚀 Como Executar

1. Certifique-se de ter o Python 3 instalado.
2. (Opcional) Crie e ative um ambiente virtual:
   ```
   python -m venv venv
   source venv/bin/activate
   ```
3. Instale a biblioteca PLY:
   ```
   pip install ply
   ```
4. Execute o analisador:
   ```
   python main.py
   ```
5. Digite ou cole os comandos da linguagem, pressione ENTER para cada linha e uma linha vazia para finalizar.
6. O arquivo `saida.html` será gerado na pasta do projeto.
7. Abra o arquivo `saida.html` em qualquer navegador para visualizar o resultado.

## 📁 Estrutura do Projeto

- `tokens.py`: Definição dos tokens e regras léxicas.
- `parser.py`: Definição da gramática e regras sintáticas.
- `main.py`: Arquivo principal que executa o analisador léxico e sintático.
- Outros arquivos conforme necessidade do projeto.


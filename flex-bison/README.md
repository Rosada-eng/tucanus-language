# Analisador Sintático com Flex-Bison

Para executar o analisador, basta rodar o programa `analyzer` utilizando o arquivo `teste.py` como entrada ou qualquer outra sequência de códigos.

```
./analyser < teste.tu
```

Para compilar novamente o executável, basta utilizar o comando abaixo

```
flex lexer.l && bison -d -t parser.y && gcc lex.yy.c parser.tab.c -o analyzer
```

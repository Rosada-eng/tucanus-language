# tucanus-language

Uma linguagem tipicamente brasileira, com uma sintaxe simples e fácil de aprender, inspirada na gramática de Python. Ideal para estudantes brasileiros, que estão tendo o primeiro contato com linguagens de programação. Aqui, você pode se concentrar em realmente aprender a lógica por trás de programação, sem se preocupar com interpretar o idioma não-nativo.

![Tucanus.tu](img/tucanus-icon1.png)

# Apresentação em Vídeo

[![Apresentação YouTube](img/tela_apresentacao.png)](https://www.youtube.com/watch?v=42cuPPkChhA&feature=youtu.be 'Apresentação no YouTube')

## EBNF

[mais detalhes aqui](https://github.com/Rosada-eng/tucanus-language/blob/main/EBNF.md)

```


-> ENBF: Tucanus

INPUT = STATEMENT, { STATEMENT, [{NEWLINE}] } ;

VAR_ASSIGNMENT =  (IDENTIFIER | VAR_DECLARATION ), "=", EXPRESSION ;
VAR_DECLARATION = "declare", IDENTIFIER;

FUNCTION_DECLARATION = "defina", IDENTIFIER, "(", PARAMETER_LIST, ")", FUNCTION_BLOCK ;


FUNCTION_CALL = IDENTIFIER, "(", (λ |PARAMETER_LIST ), ")";

STATEMENT = (     λ
                | VAR_DECLARATION
                | VAR_ASSIGNMENT
                | REL_EXPRESSION
                | FUNCTION_DECLARATION
                | FUNCTION_CALL
                | CONDITIONAL_BLOCK
                | LOOP_BLOCK
            ), "\n";

BLOCK = "{", { STATEMENT, [{NEWLINE}] }, "}" ;

FUNCTION_BLOCK = "{" , { STATEMENT, [{NEWLINE}] }, ["retorne", [PARAMETER_LIST]] , "}" ;

PARAMETER_LIST = ( λ | FACTOR, { ",", FACTOR } ) ;

LOOP_BLOCK = "enquanto for", "(", CONDITION_EVALUATION, ")", BLOCK;

CONDITIONAL_BLOCK = "se", "(", CONDITION_EVALUATION, ")", BLOCK [{( "ainda se", "(", CONDITION_EVALUATION, ")", BLOCK )}] [{( "senao", BLOCK )}];

CONDITION_EVALUATION = EVALUATION_EXPRESSION [{LOG_OP, EVALUATION_EXPRESSION}]

EVALUATION_EXPRESSION = ["!"] REL_EXPRESSION ;

REL_EXPRESSION = [{"("}] , EXPRESSION, (EVALUATION_SYMBOL | LOG_OP), EXPRESSION, [{")"}] ;

EVALUATION_SYMBOL = ( ">" | "<" | ">=" | "<=" | "==" | "!=" )

EXPRESSION = TERM, { ("+" | "-" | "||"), TERM } ;

TERM = FACTOR, { ("*" | "/" | "&&"), FACTOR } ;

FACTOR = (("+" | "-"), FACTOR) | NUMBER | "(", EXPRESSION, ")" | IDENTIFIER | LITERAL | "\n";

UN_OP = ("+" | "-" | "!");

LOG_OP = ("||" | "&&");

IDENTIFIER = LETTER { LETTER | DIGIT | "_" } ;

LITERAL = ("'" | '"'), { LETTER | DIGIT | "_" | " " }, ("'" | '"' ) ;

WORD = LETTER, { LETTER } ;

NUMBER = DIGIT, { DIGIT } ;

LETTER = ( a | ... | z | A | ... | Z ) ;

DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;


```

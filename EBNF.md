# Tucanus

Uma linguagem tipicamente brasileira, com uma sintaxe simples e fácil de aprender, inspirada na gramática de Python.

![Tucanuçu](img/tucanucu-ramphastos-toco-.webp)

---

## Visão Geral

A `<b>` EBNF `</b>` (Extended Backus-Naur Form) é uma notação usada para descrever a sintaxe de uma linguagem de programação, ou seja, as regras para escrever instruções ou expressões nessa linguagem. A seguir, uma explicação dos símbolos e construções usados nessa EBNF:

- **λ** representa a produção vazia, ou seja, uma construção que não gera nenhum símbolo terminal ou não-terminal.
- **|** representa uma escolha entre as opções à esquerda e à direita. Por exemplo, **IDENTIFIER** | **VAR_DECLARATION** indica que um **VAR_ASSIGNMENT** pode ser um identificador seguido de um sinal de igual ou uma declaração de variável seguida de um sinal de igual.
- **( )** são usados para agrupar construções em uma única produção.
- **[ ]** indica que a produção dentro dos colchetes é opcional.
- **{ }** indica que a produção dentro das chaves pode ser repetida zero ou mais vezes.
- **=** é usado para definir uma produção com um nome.
- **,** é usado para separar elementos dentro de uma produção.

Algumas definições das construções específicas usadas na EBNF abaixo:

- **VAR_ASSIGNMENT**: representa uma atribuição de valor a uma variável. Pode ser um identificador ou uma declaração de variável, seguido de um sinal de igual e uma expressão.
- **VAR_DECLARATION**: representa uma declaração de variável, com a palavra-chave "declare" seguida de um identificador.
- **FUNCTION_BLOCK**: representa um bloco de código de uma função. Consiste em uma declaração de função, um bloco de código e uma declaração de fim. A declaração de função inclui a palavra-chave "defina", um identificador, uma lista de parâmetros e um sinal de abertura de chaves. A lista de parâmetros pode ser vazia ou uma lista de identificadores separados por vírgulas.
- **FUNCTION_CALL**: representa uma chamada de função. Consiste em um identificador de função seguido de parênteses que contêm uma lista de argumentos separados por vírgulas. Os argumentos podem ser expressões, expressões de texto ou literais.
- **CONDITIONAL_BLOCK** define a sintaxe para blocos condicionais, que incluem uma declaração "se" seguida de uma condição de avaliação e um bloco de código a ser executado se a condição for verdadeira. A estrutura também permite subcondições e uma cláusula "senão" para lidar com outras possibilidades.
- **LOOP_BLOCK** define a sintaxe para um loop que continua enquanto a condição de avaliação especificada for verdadeira.
- **EXPRESSION** define a sintaxe para uma expressão matemática composta de termos e operadores aritméticos.
- **TEXT_EXPRESSION** define a sintaxe para uma expressão de texto composta de literais e identificadores.
- **LITERAL** define a sintaxe para literais de texto, que são delimitados por aspas simples ou duplas e podem incluir letras, dígitos e espaços.

---

## EBNF

```
-> ENBF: Tucanus

VAR_ASSIGNMENT =  (IDENTIFIER | VAR_DECLARATION ), "=", EXPRESSION ;
VAR_DECLARATION = "declare", IDENTIFIER;

FUNCTION_BLOCK = (FUNCTION_DECLARATION, BLOCK, END_DECLARATION) ;
FUNCTION_DECLARATION = "defina", IDENTIFIER, "(", PARAMETER_LIST, ")", "{"  ;

PARAMETER_LIST = ( λ | IDENTIFIER, { ",", IDENTIFIER } ) ;

FUNCTION_CALL = IDENTIFIER, "(",
    (    λ
        | EXPRESSION
        | TEXT_EXPRESSION
        | (IDENTIFIER | NUMBER | LITERAL), { ",", (IDENTIFIER | NUMBER | LITERAL) }
    ),
")";

CODITIONAL_BLOCK = (
    CONDITIONAL_DECLARATION, BLOCK, END_DECLARATION,
    [{( SUBCONDITIONAL_DECLARATION,  BLOCK, END_DECLARATION )}],
    [( WILDCARD_CONDITIONAL_DECLARATION,  BLOCK, END_DECLARATION )]
)

CONDITIONAL_DECLARATION = "se", "(", EVALUATION_CONDITION, ")", "{" ;
SUBCONDITIONAL_DECLARATION = "ainda se", "(", EVALUATION_CONDITION, ")", "{" ;
WILDCARD_CONDITIONAL_DECLARATION = "senao", "{" ;


LOOP_BLOCK = (LOOP_STATEMENT, BLOCK, END_DECLARATION) ;
LOOP_STATEMENT = "enquanto for", "(", EVALUATION_CONDITION, ")", "{";


EVALUATION_CONDITION = EVALUATION_EXPRESS, [{("||" | "&&") EVALUATION_EXPRESS}] ;

EVALUATION_EXPRESS = (EXPRESSION | IDENTIFIER), EVALUATION_SYMBOL , (EXPRESSION | IDENTIFIER) ;

EVALUATION_SYMBOL = ( ">" | "<" | ">=" | "<=" | "==" | "!=" )


BLOCK = { STATEMENT } ;

STATEMENT = (     λ
                | VAR_DECLARATION
                | VAR_ASSIGNMENT
                | EXPRESSION
                | FUNCTION_DECLARATION
                | FUNCTION_CALL
                | CONDITIONAL_DECLARATION
                | SUBCONDITIONAL_DECLARATION
                | WILDCARD_CONDITIONAL_DECLARATION
                | END_DECLARATION
            ), "\n";


TEXT_EXPRESSION = (IDENTIFIER | LITERAL), { "+", (IDENTIFIER | LITERAL)} ;

EXPRESSION = TERM, { ("+" | "-"), TERM } ;

TERM = FACTOR, { ("*" | "/"), FACTOR } ;

FACTOR = (("+" | "-"), FACTOR) | NUMBER | "(", EXPRESSION, ")" | IDENTIFIER ;

IDENTIFIER = LETTER { LETTER | DIGIT | "_" } ;

LITERAL = ("'" | '"'), { LETTER | DIGIT | "_" | " " }, ("'" | '"' ) ;

NUMBER = DIGIT, { DIGIT } ;

LETTER = ( a | ... | z | A | ... | Z ) ;

DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;

END_DECLARATION = "}";

```

# Tucanus

Uma linguagem tipicamente brasileira, com uma sintaxe simples e fácil de aprender, inspirada na gramática de Python.

![Tucanuçu](img/tucanucu-ramphastos-toco-.webp)

---

## Visão Geral

A **EBNF** (Extended Backus-Naur Form) é uma notação usada para descrever a sintaxe de uma linguagem de programação, ou seja, as regras para escrever instruções ou expressões nessa linguagem. A seguir, uma explicação dos símbolos e construções usados nessa EBNF:

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

INPUT = STATEMENT, { STATEMENT, [{NEWLINE}] } ;


VAR_ASSIGNMENT =  (IDENTIFIER | VAR_DECLARATION ), "=", EXPRESSION ;
VAR_DECLARATION = "declare", IDENTIFIER;

FUNCTION_DECLARATION = "defina", IDENTIFIER, "(", PARAMETER_LIST, ")", FUNCTION_BLOCK ;


FUNCTION_CALL = IDENTIFIER, "(",
    (    λ
        | PARAMETER_LIST
    ),
")";





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

END_DECLARATION = "}";

```

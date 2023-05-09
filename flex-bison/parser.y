%{
    /* definitions */
%}

/* separators */
%token COMMA SEMICOLON NEWLINE

/* delimiters */
%token OPEN_PAREN CLOSE_PAREN
%token OPEN_BRACK CLOSE_BRACK


/* arhitmetic operators */
%token PLUS MINUS MULTIPLY DIVIDER

/* logical operators */
%token AND OR NOT 
%token EQ NEQ
%token LT LTE GT GTE

/* keywords */
%token IF ELSE_IF ELSE
%token WHILE
%token DEF VAR RETURN 

/* general */
%token ASSIGNMENT
%token NUMBER
%token IDENTIFIER
%token LITERAL
%token EOL

/* non-terminal */
%type input program VAR_ASSIGNMENT VAR_DECLARATION FUNCTION_BLOCK FUNCTION_DECLARATION FUNCTION_CALL PARAMETER_LIST BLOCK STATEMENT UN_OP BIN_OP FACTOR TERM EXPRESSION

%%
    /* rules */

input:
    | STATEMENT NEWLINE input 
    | NEWLINE input
    | STATEMENT
;

STATEMENT:
    REL_EXPRESSION 
    | VAR_DECLARATION 
    | VAR_ASSIGNMENT 
    | CONDITIONAL_BLOCK
    | LOOP_BLOCK
    | FUNCTION_DECLARATION
    | FUNCTION_CALL
;


VAR_ASSIGNMENT: 
    IDENTIFIER ASSIGNMENT REL_EXPRESSION 
    | VAR_DECLARATION ASSIGNMENT REL_EXPRESSION
;

VAR_DECLARATION:
    VAR IDENTIFIER
;

FUNCTION_DECLARATION:
    DEF IDENTIFIER OPEN_PAREN PARAMETER_LIST CLOSE_PAREN FUNCTION_BLOCK
;

FUNCTION_CALL:
    IDENTIFIER OPEN_PAREN PARAMETER_LIST CLOSE_PAREN
;

PARAMETER_LIST:
    
    | FACTOR
    | PARAMETER_LIST COMMA PARAMETER_LIST

BLOCK:
    OPEN_BRACK input CLOSE_BRACK
;

FUNCTION_BLOCK:
    OPEN_BRACK input RETURN PARAMETER_LIST NEWLINE CLOSE_BRACK
    | OPEN_BRACK input CLOSE_BRACK
;

LOOP_BLOCK:
    WHILE OPEN_PAREN CONDITION_EVALUATION CLOSE_PAREN BLOCK

CONDITIONAL_BLOCK:
    IF OPEN_PAREN CONDITION_EVALUATION CLOSE_PAREN BLOCK
    | CONDITIONAL_BLOCK ELSE_IF OPEN_PAREN CONDITION_EVALUATION CLOSE_PAREN BLOCK
    | CONDITIONAL_BLOCK ELSE BLOCK
;

CONDITION_EVALUATION:
    EVALUATION_EXPRESSION
    | EVALUATION_EXPRESSION LOG_OP EVALUATION_EXPRESSION 
;

EVALUATION_EXPRESSION:
    REL_EXPRESSION
    | NOT EVALUATION_EXPRESSION
;

EVALUATION_SYMBOL:
    EQ
    | NEQ
    | LT
    | LTE
    | GT
    | GTE
;

REL_EXPRESSION:
    EXPRESSION
    | REL_EXPRESSION EVALUATION_SYMBOL REL_EXPRESSION
    | REL_EXPRESSION LOG_OP REL_EXPRESSION
    | OPEN_PAREN REL_EXPRESSION CLOSE_PAREN
;

EXPRESSION:
    TERM
    | EXPRESSION PLUS EXPRESSION
    | EXPRESSION MINUS EXPRESSION
    | EXPRESSION OR EXPRESSION
;

TERM:
    FACTOR
    | TERM MULTIPLY TERM
    | TERM DIVIDER TERM
    | TERM AND TERM
;

FACTOR:
    NUMBER
    | IDENTIFIER
    | UN_OP FACTOR
    | LITERAL
    | OPEN_PAREN EXPRESSION CLOSE_PAREN
    | NEWLINE
;

UN_OP:
    PLUS
    | MINUS
    | NOT
;

LOG_OP:
    AND
    | OR
;

%%

int main() {
    yyparse();


    return 0;
}

yyerror(char* s)
{
    printf("ERROR %s\n", s);

    return 0;
}
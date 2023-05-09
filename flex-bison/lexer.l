/*** Definition Section (C stuff) ***/
%{
	#include <stdio.h>
	#include "parser.tab.h"
	
	#define SAVE_TOKEN yylval.string = new std::string(yytext, yyleng);
	#define TOKEN(t) (yylval.token = t)

    int count = 0;
	
%}



%%
[0-9]+		{printf("Digit: %s\n",yytext); count++; return NUMBER; }
"se" 		{printf("se: %s\n",yytext); count++; return IF; }
"ainda se"  {printf("ainda se: %s\n",yytext); count++; return ELSE_IF;}
"senao" 	{printf("senão: %s\n",yytext); count++; return ELSE;}

"enquanto for" 		{printf("enquanto for: %s\n",yytext); count++; return WHILE; }

"defina" 	{printf("defina: %s\n",yytext); count++; return DEF;}

"declare" 	{printf("declare: %s\n",yytext); count++; return VAR;}

"retornar" 	{printf("retornar: %s\n",yytext); count++; return RETURN;}


["].+["]		{printf("String: %s\n",yytext); count++; return LITERAL; }
"<" 		{printf("Less than: %s\n",yytext); count++; return LT;}
">"			{printf("Greater than: %s\n",yytext); count++; return GT;}
"=="		{printf("Equal to: %s\n",yytext); count++; return EQ;}
"="			{printf("Assign to: %s\n",yytext); count++; return ASSIGNMENT;}
"!=" 		{printf("Not equal to: %s\n",yytext); count++; return NEQ;}
"<=" 		{printf("Less than or equal to: %s\n",yytext); count++; return LTE;}
">=" 		{printf("Greater than or equal to: %s\n",yytext); count++; return GTE;}

"&&" 		{printf("Logical AND: %s\n",yytext); count++; return AND;}
"||" 		{printf("Logical OR: %s\n",yytext); count++; return OR;}
"!" 		{printf("Logical NOT: %s\n",yytext); count++; return NOT;}

"(" 		{printf("Left Parenthesis: %s\n",yytext); count++; return OPEN_PAREN;}
")" 		{printf("Right Parenthesis: %s\n",yytext); count++; return CLOSE_PAREN;}

"{" 		{printf("Left Curly Brace: %s\n",yytext); count++; return OPEN_BRACK;}
"}" 		{printf("Right Curly Brace: %s\n",yytext); count++; return CLOSE_BRACK; }

"+" 		{printf("Plus: %s\n",yytext); count++; return PLUS; }
"-" 		{printf("Minus: %s\n",yytext); count++; return MINUS;}
"*" 		{printf("Multiplication: %s\n",yytext); count++; return MULTIPLY;}
"/" 		{printf("Division: %s\n",yytext); count++; return DIVIDER;}
"," 		{printf("Comma: %s\n",yytext); count++; return COMMA;}




[a-zA-Z_][a-zA-Z0-9_]*	{printf("Identifier: %s\n",yytext); count++; return IDENTIFIER; }

\n			{printf("Newline: \\n \n"); count++; return NEWLINE; }
[ \t] 	

%%

yywrap() {}


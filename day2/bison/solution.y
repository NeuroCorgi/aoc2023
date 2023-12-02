%{
#include "solution.h"
#include <stdio.h>

int yylex(void);
int yyerror(const char *);
%}


%code requires {
#include "solution.h"
}

%define parse.error verbose

%token GAME NUMBER RED GREEN BLUE
%union {
  int intval;
  unsigned int uintval;
  group_t groupval;
}

%type <uintval> data
%type <uintval> input
%type <uintval> game
%type <groupval> group_list
%type <groupval> group
%type <groupval> cube
%type <uintval> NUMBER

%%

data: input { $$ = $1; printf("%d\n", $$); }

input: /* empty */  { $$ = 0; }
  | game '\n' input { $$ = $1 + $3; }
  | game            { $$ = $1; }
  ;

game: GAME NUMBER ':' group_list { $$ = groupPower($4); };

group_list: group_list ';' group { $$ = groupUnion($1, $3); }
          | group                { $$ = $1; }
; 

group :
    cube ',' cube ',' cube { $$ = groupUnion($1, groupUnion($3, $5)); }
  | cube ',' cube          { $$ = groupUnion($1, $3); }
  | cube                   { $$ = $1; }
  ;

cube :
    NUMBER RED   { $$ = red($1); }
  | NUMBER GREEN { $$ = green($1); }
  | NUMBER BLUE  { $$ = blue($1); }
  ;

%%

int main() {
	yyparse();
	return 0;
}

int yyerror(const char *s) {
	fprintf(stderr, "Parse error: %s\n", s);
	return 1;
}

%{
#include "solution.tab.h"
%}

%%

"Game"    { return GAME;  }
"red"     { return RED;   }
"green"   { return GREEN; }
"blue"    { return BLUE;  }
","       { return ','; }
";"       { return ';'; }
":"       { return ':'; }
"\n"      { return '\n'; }
[0-9]+    { yylval.intval = atoi(yytext);
            return NUMBER;
          }    
[ \t]     {}

%%

int yywrap() {
    return 1;
}

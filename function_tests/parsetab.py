
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftNOTANDORleftEQUALSLTLENEGTGEleftCONCATleftINleftPLUSMINUSleftTIMESDIVIDEDIVMODrightPOWERleftTUPLEINDEXrightUMINUSAND ASSIGN BOOLEAN COMMA CONCAT DIV DIVIDE ELSE EQUALS FUN GE GT ID IF IN LBRACKET LCURLY LE LPAREN LT MINUS MOD NE NOT NUMBER OR PLUS POWER PRINT RBRACKET RCURLY RPAREN SEMICOLON STRING TIMES TUPLEINDEX WHILEprogram : functions blockfunctions : functions functionfunctions : functionfunction : FUN ID LPAREN params RPAREN ASSIGN block expression SEMICOLONparams : params COMMA IDparams : IDexpression : function_call\n       factor     : function_call\n       list       : function_call\n       string     : function_call\n       tuple      : function_callstatement : expression SEMICOLONfunction_call : ID LPAREN args RPARENargs : args COMMA expressionargs : expressionblock : LCURLY statement_list RCURLYstatement_list : statement_list statementstatement_list : statementstatement : assign_statement\n                 | print_statement\n                 | conditional_statement\n                 | while_statement\n                 | empty_statement\n                 | blockvariable : IDassign_statement : variable ASSIGN expression SEMICOLONassign_statement : ID LBRACKET expression RBRACKET ASSIGN expression SEMICOLONprint_statement : PRINT LPAREN expression RPAREN SEMICOLONconditional_statement : if_statement\n                             | if_else_statementif_statement : IF LPAREN expression RPAREN blockif_else_statement : IF LPAREN expression RPAREN block ELSE blockwhile_statement : WHILE LPAREN expression RPAREN blockempty_statement : factor     : ID\n       list       : ID\n       string     : ID\n       tuple      : ID\n       expression : IDexpression : LPAREN expression RPARENexpression : expression PLUS expression\n                  | expression MINUS expressionexpression : termterm : term TIMES factor\n            | term DIVIDE factor\n            | factor POWER term\n            | term DIV factor\n            | term MOD factorterm : factorfactor : LPAREN expression RPARENfactor : NUMBERfactor : MINUS factor %prec UMINUSexpression : stringstring : STRINGexpression : string PLUS expressionexpression : string LBRACKET expression RBRACKETexpression : listlist : LBRACKET taillist : LBRACKET expression tailtail : COMMA expression tailtail : RBRACKETlist : list PLUS listexpression : list LBRACKET expression RBRACKETlist : list LBRACKET expression RBRACKETexpression : tupletuple : LPAREN expression tupletailtupletail : COMMA expression tupletailtupletail : RPARENexpression : TUPLEINDEX expression tupletuple : TUPLEINDEX expression tupleboolean : expression IN expressionlist : expression CONCAT listboolean : expression LT expression\n               | expression LE expression\n               | expression EQUALS expression\n               | expression NE expression\n               | expression GT expression\n               | expression GE expressionexpression : booleanboolean : BOOLEANexpression : NOT expressionexpression : expression AND expression\n                  | expression OR expression'
    
_lr_action_items = {'FUN':([0,2,3,6,162,],[4,4,-3,-2,-4,]),'$end':([1,5,41,],[0,-1,-16,]),'LCURLY':([2,3,6,7,9,10,12,13,14,15,16,17,32,33,41,42,43,140,142,143,144,152,153,154,158,160,161,162,],[7,-3,-2,7,7,-18,-19,-20,-21,-22,-23,-24,-29,-30,-16,-17,-12,-26,7,7,7,-28,-33,-31,7,-27,-32,-4,]),'ID':([4,7,9,10,12,13,14,15,16,17,18,20,21,22,23,24,25,26,27,28,29,32,33,35,36,37,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,59,60,61,62,63,64,65,66,67,68,69,70,72,73,74,75,76,77,78,79,80,81,82,85,86,87,88,90,91,92,93,94,95,96,97,98,99,103,104,105,107,108,109,110,111,113,116,117,118,119,120,121,125,128,129,131,132,134,135,136,137,138,140,147,149,150,151,152,153,154,155,156,160,161,],[8,19,19,-18,-19,-20,-21,-22,-23,-24,-7,59,62,-43,-53,59,-57,-65,59,-79,59,-29,-30,-49,-54,-80,-51,83,-16,-17,-12,59,59,59,59,92,59,59,59,59,59,59,59,59,59,-35,-52,-8,-35,59,62,62,62,62,59,59,-58,59,-61,59,92,120,-81,59,59,59,62,59,-41,-42,-82,-83,-72,-9,-36,-71,-73,-74,-75,-76,-77,-78,-40,-66,59,-44,-45,-47,-48,-55,-59,-62,59,-69,-11,-38,59,-46,145,59,-13,59,-50,-56,-60,-63,120,-26,59,-67,-68,-70,-28,-33,-31,59,-64,-27,-32,]),'LPAREN':([7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,31,32,33,34,35,36,37,38,39,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,59,60,61,62,63,64,65,66,67,68,69,70,72,73,74,75,76,77,78,79,80,81,82,85,86,87,88,90,91,92,93,94,95,96,97,98,99,103,104,105,107,108,109,110,111,113,116,117,118,119,120,121,125,129,131,132,134,135,136,137,138,140,147,149,150,151,152,153,154,155,156,160,161,],[20,40,20,-18,-19,-20,-21,-22,-23,-24,-7,57,20,63,-43,-53,20,-57,-65,20,-79,20,79,-29,-30,80,-49,-54,-80,82,-51,-16,-17,-12,20,20,20,20,20,20,20,20,20,20,20,20,20,20,57,-52,-8,57,20,63,63,63,63,20,20,-58,20,-61,20,20,121,-81,20,20,20,63,20,-41,-42,-82,-83,-72,-9,57,-71,-73,-74,-75,-76,-77,-78,-40,-66,20,-44,-45,-47,-48,-55,-59,-62,20,-69,-11,57,20,-46,20,-13,20,-50,-56,-60,-63,121,-26,20,-67,-68,-70,-28,-33,-31,20,-64,-27,-32,]),'TUPLEINDEX':([7,9,10,12,13,14,15,16,17,18,20,22,23,24,25,26,27,28,29,32,33,35,36,37,39,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,59,60,61,62,63,68,69,70,72,73,74,75,76,77,78,79,80,82,85,86,87,88,90,91,92,93,94,95,96,97,98,99,103,104,105,107,108,109,110,111,113,116,117,118,119,120,121,125,129,131,132,134,135,136,137,138,140,147,149,150,151,152,153,154,155,156,160,161,],[27,27,-18,-19,-20,-21,-22,-23,-24,-7,27,-43,-53,27,-57,-65,27,-79,27,-29,-30,-49,-54,-80,-51,-16,-17,-12,27,27,27,27,27,27,27,27,27,27,27,27,27,27,-35,-52,-8,-35,27,27,27,-58,27,-61,27,27,117,-81,27,27,27,27,-41,-42,-82,-83,-72,-9,-36,-71,-73,-74,-75,-76,-77,-78,-40,-66,27,-44,-45,-47,-48,-55,-59,-62,27,-69,-11,-38,27,-46,27,-13,27,-50,-56,-60,-63,117,-26,27,-67,-68,-70,-28,-33,-31,27,-64,-27,-32,]),'NOT':([7,9,10,12,13,14,15,16,17,20,24,27,29,32,33,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,63,68,69,72,74,75,78,79,80,82,105,117,121,129,132,140,147,152,153,154,155,160,161,],[29,29,-18,-19,-20,-21,-22,-23,-24,29,29,29,29,-29,-30,-16,-17,-12,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,-26,29,-28,-33,-31,29,-27,-32,]),'PRINT':([7,9,10,12,13,14,15,16,17,32,33,41,42,43,140,152,153,154,160,161,],[31,31,-18,-19,-20,-21,-22,-23,-24,-29,-30,-16,-17,-12,-26,-28,-33,-31,-27,-32,]),'WHILE':([7,9,10,12,13,14,15,16,17,32,33,41,42,43,140,152,153,154,160,161,],[34,34,-18,-19,-20,-21,-22,-23,-24,-29,-30,-16,-17,-12,-26,-28,-33,-31,-27,-32,]),'RCURLY':([7,9,10,12,13,14,15,16,17,32,33,41,42,43,140,152,153,154,160,161,],[-34,41,-18,-19,-20,-21,-22,-23,-24,-29,-30,-16,-17,-12,-26,-28,-33,-31,-27,-32,]),'STRING':([7,9,10,12,13,14,15,16,17,20,24,27,29,32,33,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,63,68,69,72,74,75,78,79,80,82,105,117,121,129,132,140,147,152,153,154,155,160,161,],[36,36,-18,-19,-20,-21,-22,-23,-24,36,36,36,36,-29,-30,-16,-17,-12,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,-26,36,-28,-33,-31,36,-27,-32,]),'LBRACKET':([7,9,10,12,13,14,15,16,17,18,19,20,23,24,25,27,29,32,33,36,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,59,63,68,69,70,72,73,74,75,78,79,80,82,90,91,92,105,113,116,117,121,129,131,132,136,137,140,147,152,153,154,155,156,160,161,],[24,24,-18,-19,-20,-21,-22,-23,-24,-9,56,24,69,24,74,24,24,-29,-30,-54,-16,-17,-12,24,24,24,24,24,24,24,24,24,24,24,24,24,24,-36,24,24,24,-58,24,-61,24,24,24,24,24,24,-72,-9,-36,24,-59,-62,24,24,24,-13,24,-60,-64,-26,24,-28,-33,-31,24,-64,-27,-32,]),'BOOLEAN':([7,9,10,12,13,14,15,16,17,20,24,27,29,32,33,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,63,68,69,72,74,75,78,79,80,82,105,117,121,129,132,140,147,152,153,154,155,160,161,],[37,37,-18,-19,-20,-21,-22,-23,-24,37,37,37,37,-29,-30,-16,-17,-12,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,-26,37,-28,-33,-31,37,-27,-32,]),'IF':([7,9,10,12,13,14,15,16,17,32,33,41,42,43,140,152,153,154,160,161,],[38,38,-18,-19,-20,-21,-22,-23,-24,-29,-30,-16,-17,-12,-26,-28,-33,-31,-27,-32,]),'NUMBER':([7,9,10,12,13,14,15,16,17,20,21,24,27,29,32,33,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,63,64,65,66,67,68,69,72,74,75,78,79,80,81,82,105,117,121,129,132,140,147,152,153,154,155,160,161,],[39,39,-18,-19,-20,-21,-22,-23,-24,39,39,39,39,39,-29,-30,-16,-17,-12,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,-26,39,-28,-33,-31,39,-27,-32,]),'MINUS':([7,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,32,33,35,36,37,39,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,129,131,132,133,134,135,136,137,138,139,140,146,147,148,149,150,151,152,153,154,155,156,157,159,160,161,],[21,21,-18,45,-19,-20,-21,-22,-23,-24,-7,-35,21,21,-43,-53,21,-57,-65,21,-79,21,-29,-30,-49,-54,-80,-51,-16,-17,-12,21,21,21,21,21,21,21,21,21,21,21,21,21,21,45,-35,-52,-8,-35,21,21,21,21,21,21,21,-58,45,21,-61,21,21,45,45,21,21,21,21,21,-41,-42,45,45,45,-57,-7,-35,45,45,45,45,45,45,45,45,45,-40,-66,21,45,-44,-45,-47,-48,-55,45,-59,45,45,-57,21,-69,-11,-38,21,45,45,45,-46,45,21,-13,21,45,-50,-56,-60,-63,45,45,-26,45,21,45,-67,-68,-70,-28,-33,-31,21,-63,45,45,-27,-32,]),'SEMICOLON':([11,18,19,22,23,25,26,28,35,36,37,39,59,60,61,62,70,73,77,85,86,87,88,90,91,92,93,94,95,96,97,98,99,103,104,107,108,109,110,111,113,116,118,119,120,122,125,131,134,135,136,137,141,149,150,151,156,157,159,],[43,-7,-35,-43,-53,-57,-65,-79,-49,-54,-80,-51,-35,-52,-8,-35,-58,-61,-81,-41,-42,-82,-83,-72,-9,-36,-71,-73,-74,-75,-76,-77,-78,-40,-66,-44,-45,-47,-48,-55,-59,-62,-69,-11,-38,140,-46,-13,-50,-56,-60,-63,152,-67,-68,-70,-64,160,162,]),'PLUS':([11,18,19,22,23,25,26,28,35,36,37,39,58,59,60,61,62,70,71,73,76,77,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,104,106,107,108,109,110,111,112,113,114,115,116,118,119,120,122,123,124,125,126,131,133,134,135,136,137,138,139,146,148,149,150,151,156,157,159,],[44,-7,-35,-43,68,75,-65,-79,-49,-54,-80,-51,44,-35,-52,-8,-35,-58,44,-61,44,44,-41,-42,44,44,44,75,-7,-35,44,44,44,44,44,44,44,44,44,-40,-66,44,-44,-45,-47,-48,-55,44,-59,44,44,-57,-69,-11,-38,44,44,44,-46,44,-13,44,-50,-56,-60,-63,44,44,44,44,-67,-68,-70,-63,44,44,]),'AND':([11,18,19,22,23,25,26,28,35,36,37,39,58,59,60,61,62,70,71,73,76,77,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,104,106,107,108,109,110,111,112,113,114,115,116,118,119,120,122,123,124,125,126,131,133,134,135,136,137,138,139,146,148,149,150,151,156,157,159,],[46,-7,-35,-43,-53,-57,-65,-79,-49,-54,-80,-51,46,-35,-52,-8,-35,-58,46,-61,46,-81,-41,-42,-82,-83,46,-57,-7,-35,-71,-73,-74,-75,-76,-77,-78,46,46,-40,-66,46,-44,-45,-47,-48,-55,46,-59,46,46,-57,-69,-11,-38,46,46,46,-46,46,-13,46,-50,-56,-60,-63,46,46,46,46,-67,-68,-70,-63,46,46,]),'OR':([11,18,19,22,23,25,26,28,35,36,37,39,58,59,60,61,62,70,71,73,76,77,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,104,106,107,108,109,110,111,112,113,114,115,116,118,119,120,122,123,124,125,126,131,133,134,135,136,137,138,139,146,148,149,150,151,156,157,159,],[47,-7,-35,-43,-53,-57,-65,-79,-49,-54,-80,-51,47,-35,-52,-8,-35,-58,47,-61,47,-81,-41,-42,-82,-83,47,-57,-7,-35,-71,-73,-74,-75,-76,-77,-78,47,47,-40,-66,47,-44,-45,-47,-48,-55,47,-59,47,47,-57,-69,-11,-38,47,47,47,-46,47,-13,47,-50,-56,-60,-63,47,47,47,47,-67,-68,-70,-63,47,47,]),'CONCAT':([11,18,19,22,23,25,26,28,35,36,37,39,58,59,60,61,62,70,71,73,76,77,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,104,106,107,108,109,110,111,112,113,114,115,116,118,119,120,122,123,124,125,126,131,133,134,135,136,137,138,139,146,148,149,150,151,156,157,159,],[48,-7,-35,-43,-53,-57,-65,-79,-49,-54,-80,-51,48,-35,-52,-8,-35,-58,48,-61,48,48,-41,-42,48,48,48,-57,-7,-35,-71,48,48,48,48,48,48,48,48,-40,-66,48,-44,-45,-47,-48,-55,48,-59,48,48,-57,-69,-11,-38,48,48,48,-46,48,-13,48,-50,-56,-60,-63,48,48,48,48,-67,-68,-70,-63,48,48,]),'IN':([11,18,19,22,23,25,26,28,35,36,37,39,58,59,60,61,62,70,71,73,76,77,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,104,106,107,108,109,110,111,112,113,114,115,116,118,119,120,122,123,124,125,126,131,133,134,135,136,137,138,139,146,148,149,150,151,156,157,159,],[49,-7,-35,-43,-53,-57,-65,-79,-49,-54,-80,-51,49,-35,-52,-8,-35,-58,49,-61,49,49,-41,-42,49,49,49,-57,-7,-35,-71,49,49,49,49,49,49,49,49,-40,-66,49,-44,-45,-47,-48,-55,49,-59,49,49,-57,-69,-11,-38,49,49,49,-46,49,-13,49,-50,-56,-60,-63,49,49,49,49,-67,-68,-70,-63,49,49,]),'LT':([11,18,19,22,23,25,26,28,35,36,37,39,58,59,60,61,62,70,71,73,76,77,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,104,106,107,108,109,110,111,112,113,114,115,116,118,119,120,122,123,124,125,126,131,133,134,135,136,137,138,139,146,148,149,150,151,156,157,159,],[50,-7,-35,-43,-53,-57,-65,-79,-49,-54,-80,-51,50,-35,-52,-8,-35,-58,50,-61,50,50,-41,-42,50,50,50,-57,-7,-35,-71,-73,-74,-75,-76,-77,-78,50,50,-40,-66,50,-44,-45,-47,-48,-55,50,-59,50,50,-57,-69,-11,-38,50,50,50,-46,50,-13,50,-50,-56,-60,-63,50,50,50,50,-67,-68,-70,-63,50,50,]),'LE':([11,18,19,22,23,25,26,28,35,36,37,39,58,59,60,61,62,70,71,73,76,77,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,104,106,107,108,109,110,111,112,113,114,115,116,118,119,120,122,123,124,125,126,131,133,134,135,136,137,138,139,146,148,149,150,151,156,157,159,],[51,-7,-35,-43,-53,-57,-65,-79,-49,-54,-80,-51,51,-35,-52,-8,-35,-58,51,-61,51,51,-41,-42,51,51,51,-57,-7,-35,-71,-73,-74,-75,-76,-77,-78,51,51,-40,-66,51,-44,-45,-47,-48,-55,51,-59,51,51,-57,-69,-11,-38,51,51,51,-46,51,-13,51,-50,-56,-60,-63,51,51,51,51,-67,-68,-70,-63,51,51,]),'EQUALS':([11,18,19,22,23,25,26,28,35,36,37,39,58,59,60,61,62,70,71,73,76,77,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,104,106,107,108,109,110,111,112,113,114,115,116,118,119,120,122,123,124,125,126,131,133,134,135,136,137,138,139,146,148,149,150,151,156,157,159,],[52,-7,-35,-43,-53,-57,-65,-79,-49,-54,-80,-51,52,-35,-52,-8,-35,-58,52,-61,52,52,-41,-42,52,52,52,-57,-7,-35,-71,-73,-74,-75,-76,-77,-78,52,52,-40,-66,52,-44,-45,-47,-48,-55,52,-59,52,52,-57,-69,-11,-38,52,52,52,-46,52,-13,52,-50,-56,-60,-63,52,52,52,52,-67,-68,-70,-63,52,52,]),'NE':([11,18,19,22,23,25,26,28,35,36,37,39,58,59,60,61,62,70,71,73,76,77,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,104,106,107,108,109,110,111,112,113,114,115,116,118,119,120,122,123,124,125,126,131,133,134,135,136,137,138,139,146,148,149,150,151,156,157,159,],[53,-7,-35,-43,-53,-57,-65,-79,-49,-54,-80,-51,53,-35,-52,-8,-35,-58,53,-61,53,53,-41,-42,53,53,53,-57,-7,-35,-71,-73,-74,-75,-76,-77,-78,53,53,-40,-66,53,-44,-45,-47,-48,-55,53,-59,53,53,-57,-69,-11,-38,53,53,53,-46,53,-13,53,-50,-56,-60,-63,53,53,53,53,-67,-68,-70,-63,53,53,]),'GT':([11,18,19,22,23,25,26,28,35,36,37,39,58,59,60,61,62,70,71,73,76,77,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,104,106,107,108,109,110,111,112,113,114,115,116,118,119,120,122,123,124,125,126,131,133,134,135,136,137,138,139,146,148,149,150,151,156,157,159,],[54,-7,-35,-43,-53,-57,-65,-79,-49,-54,-80,-51,54,-35,-52,-8,-35,-58,54,-61,54,54,-41,-42,54,54,54,-57,-7,-35,-71,-73,-74,-75,-76,-77,-78,54,54,-40,-66,54,-44,-45,-47,-48,-55,54,-59,54,54,-57,-69,-11,-38,54,54,54,-46,54,-13,54,-50,-56,-60,-63,54,54,54,54,-67,-68,-70,-63,54,54,]),'GE':([11,18,19,22,23,25,26,28,35,36,37,39,58,59,60,61,62,70,71,73,76,77,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,104,106,107,108,109,110,111,112,113,114,115,116,118,119,120,122,123,124,125,126,131,133,134,135,136,137,138,139,146,148,149,150,151,156,157,159,],[55,-7,-35,-43,-53,-57,-65,-79,-49,-54,-80,-51,55,-35,-52,-8,-35,-58,55,-61,55,55,-41,-42,55,55,55,-57,-7,-35,-71,-73,-74,-75,-76,-77,-78,55,55,-40,-66,55,-44,-45,-47,-48,-55,55,-59,55,55,-57,-69,-11,-38,55,55,55,-46,55,-13,55,-50,-56,-60,-63,55,55,55,55,-67,-68,-70,-63,55,55,]),'RPAREN':([18,22,23,25,26,28,35,36,37,39,58,59,60,61,62,70,73,77,83,84,85,86,87,88,90,91,92,93,94,95,96,97,98,99,101,102,103,104,106,107,108,109,110,111,113,116,118,119,120,123,124,125,126,131,133,134,135,136,137,139,145,148,149,150,151,156,],[-7,-43,-53,-57,-65,-79,-49,-54,-80,-51,103,-35,-52,-8,-35,-58,-61,-81,-6,127,-41,-42,-82,-83,-72,-9,-36,-71,-73,-74,-75,-76,-77,-78,131,-15,-40,-66,134,-44,-45,-47,-48,-55,-59,-62,-69,-11,-38,141,142,-46,143,-13,150,-50,-56,-60,-63,150,-5,-14,-67,-68,-70,-64,]),'COMMA':([18,22,23,24,25,26,28,35,36,37,39,58,59,60,61,62,70,71,73,77,83,84,85,86,87,88,90,91,92,93,94,95,96,97,98,99,101,102,103,104,107,108,109,110,111,113,114,116,118,119,120,125,131,133,134,135,136,137,139,145,148,149,150,151,156,],[-7,-43,-53,72,-57,-65,-79,-49,-54,-80,-51,105,-35,-52,-8,-35,-58,72,-61,-81,-6,128,-41,-42,-82,-83,-72,-9,-36,-71,-73,-74,-75,-76,-77,-78,132,-15,-40,-66,-44,-45,-47,-48,-55,-59,72,-62,-69,-11,-38,-46,-13,105,-50,-56,-60,-63,105,-5,-14,-67,-68,-70,-64,]),'RBRACKET':([18,22,23,24,25,26,28,35,36,37,39,59,60,61,62,70,71,73,77,85,86,87,88,90,91,92,93,94,95,96,97,98,99,100,103,104,107,108,109,110,111,112,113,114,115,116,118,119,120,125,131,134,135,136,137,146,149,150,151,156,],[-7,-43,-53,73,-57,-65,-79,-49,-54,-80,-51,-35,-52,-8,-35,-58,73,-61,-81,-41,-42,-82,-83,-72,-9,-36,-71,-73,-74,-75,-76,-77,-78,130,-40,-66,-44,-45,-47,-48,-55,135,-59,73,137,-62,-69,-11,-38,-46,-13,-50,-56,-60,-63,156,-67,-68,-70,-64,]),'POWER':([18,19,35,39,59,60,61,62,91,92,103,131,134,],[-8,-35,81,-51,-35,-52,-8,-35,-8,-35,-50,-13,-50,]),'TIMES':([18,19,22,35,39,59,60,61,62,91,92,103,107,108,109,110,125,131,134,],[-8,-35,64,-49,-51,-35,-52,-8,-35,-8,-35,-50,-44,-45,-47,-48,-46,-13,-50,]),'DIVIDE':([18,19,22,35,39,59,60,61,62,91,92,103,107,108,109,110,125,131,134,],[-8,-35,65,-49,-51,-35,-52,-8,-35,-8,-35,-50,-44,-45,-47,-48,-46,-13,-50,]),'DIV':([18,19,22,35,39,59,60,61,62,91,92,103,107,108,109,110,125,131,134,],[-8,-35,66,-49,-51,-35,-52,-8,-35,-8,-35,-50,-44,-45,-47,-48,-46,-13,-50,]),'MOD':([18,19,22,35,39,59,60,61,62,91,92,103,107,108,109,110,125,131,134,],[-8,-35,67,-49,-51,-35,-52,-8,-35,-8,-35,-50,-44,-45,-47,-48,-46,-13,-50,]),'ASSIGN':([19,30,127,130,],[-25,78,144,147,]),'ELSE':([41,154,],[-16,158,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'functions':([0,],[2,]),'function':([0,2,],[3,6,]),'block':([2,7,9,142,143,144,158,],[5,17,17,153,154,155,161,]),'statement_list':([7,],[9,]),'statement':([7,9,],[10,42,]),'expression':([7,9,20,24,27,29,44,45,46,47,48,49,50,51,52,53,54,55,56,57,63,68,69,72,74,75,78,79,80,82,105,117,121,129,132,147,155,],[11,11,58,71,76,77,85,86,87,88,89,93,94,95,96,97,98,99,100,102,106,111,112,114,115,89,122,123,124,126,133,138,139,146,148,157,159,]),'assign_statement':([7,9,],[12,12,]),'print_statement':([7,9,],[13,13,]),'conditional_statement':([7,9,],[14,14,]),'while_statement':([7,9,],[15,15,]),'empty_statement':([7,9,],[16,16,]),'function_call':([7,9,20,21,24,27,29,44,45,46,47,48,49,50,51,52,53,54,55,56,57,63,64,65,66,67,68,69,72,74,75,76,78,79,80,81,82,105,117,121,129,132,138,147,155,],[18,18,18,61,18,18,18,18,18,18,18,91,18,18,18,18,18,18,18,18,18,18,61,61,61,61,18,18,18,18,91,119,18,18,18,61,18,18,18,18,18,18,119,18,18,]),'term':([7,9,20,24,27,29,44,45,46,47,48,49,50,51,52,53,54,55,56,57,63,68,69,72,74,75,78,79,80,81,82,105,117,121,129,132,147,155,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,125,22,22,22,22,22,22,22,22,]),'string':([7,9,20,24,27,29,44,45,46,47,48,49,50,51,52,53,54,55,56,57,63,68,69,72,74,75,78,79,80,82,105,117,121,129,132,147,155,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'list':([7,9,20,24,27,29,44,45,46,47,48,49,50,51,52,53,54,55,56,57,63,68,69,72,74,75,78,79,80,82,105,117,121,129,132,147,155,],[25,25,25,25,25,25,25,25,25,25,90,25,25,25,25,25,25,25,25,25,25,25,25,25,25,116,25,25,25,25,25,25,25,25,25,25,25,]),'tuple':([7,9,20,24,27,29,44,45,46,47,48,49,50,51,52,53,54,55,56,57,63,68,69,72,74,75,76,78,79,80,82,105,117,121,129,132,138,147,155,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,118,26,26,26,26,26,26,26,26,26,151,26,26,]),'boolean':([7,9,20,24,27,29,44,45,46,47,48,49,50,51,52,53,54,55,56,57,63,68,69,72,74,75,78,79,80,82,105,117,121,129,132,147,155,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'variable':([7,9,],[30,30,]),'if_statement':([7,9,],[32,32,]),'if_else_statement':([7,9,],[33,33,]),'factor':([7,9,20,21,24,27,29,44,45,46,47,48,49,50,51,52,53,54,55,56,57,63,64,65,66,67,68,69,72,74,75,78,79,80,81,82,105,117,121,129,132,147,155,],[35,35,35,60,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,107,108,109,110,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'tail':([24,71,114,],[70,113,136,]),'params':([40,],[84,]),'args':([57,],[101,]),'tupletail':([58,133,139,],[104,149,104,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> functions block','program',2,'p_program','sbml.py',598),
  ('functions -> functions function','functions',2,'p_functions0','sbml.py',602),
  ('functions -> function','functions',1,'p_functions1','sbml.py',606),
  ('function -> FUN ID LPAREN params RPAREN ASSIGN block expression SEMICOLON','function',9,'p_function','sbml.py',610),
  ('params -> params COMMA ID','params',3,'p_params0','sbml.py',615),
  ('params -> ID','params',1,'p_params1','sbml.py',619),
  ('expression -> function_call','expression',1,'p_expression_function_call','sbml.py',623),
  ('factor -> function_call','factor',1,'p_expression_function_call','sbml.py',624),
  ('list -> function_call','list',1,'p_expression_function_call','sbml.py',625),
  ('string -> function_call','string',1,'p_expression_function_call','sbml.py',626),
  ('tuple -> function_call','tuple',1,'p_expression_function_call','sbml.py',627),
  ('statement -> expression SEMICOLON','statement',2,'p_statement_expression','sbml.py',631),
  ('function_call -> ID LPAREN args RPAREN','function_call',4,'p_function_call','sbml.py',635),
  ('args -> args COMMA expression','args',3,'p_args0','sbml.py',639),
  ('args -> expression','args',1,'p_args1','sbml.py',643),
  ('block -> LCURLY statement_list RCURLY','block',3,'p_block','sbml.py',648),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','sbml.py',652),
  ('statement_list -> statement','statement_list',1,'p_statement_list_val','sbml.py',656),
  ('statement -> assign_statement','statement',1,'p_statement','sbml.py',660),
  ('statement -> print_statement','statement',1,'p_statement','sbml.py',661),
  ('statement -> conditional_statement','statement',1,'p_statement','sbml.py',662),
  ('statement -> while_statement','statement',1,'p_statement','sbml.py',663),
  ('statement -> empty_statement','statement',1,'p_statement','sbml.py',664),
  ('statement -> block','statement',1,'p_statement','sbml.py',665),
  ('variable -> ID','variable',1,'p_variable_ID','sbml.py',671),
  ('assign_statement -> variable ASSIGN expression SEMICOLON','assign_statement',4,'p_assign_statement1','sbml.py',675),
  ('assign_statement -> ID LBRACKET expression RBRACKET ASSIGN expression SEMICOLON','assign_statement',7,'p_assign_statement2','sbml.py',679),
  ('print_statement -> PRINT LPAREN expression RPAREN SEMICOLON','print_statement',5,'p_print_statement','sbml.py',685),
  ('conditional_statement -> if_statement','conditional_statement',1,'p_conditional_statement','sbml.py',691),
  ('conditional_statement -> if_else_statement','conditional_statement',1,'p_conditional_statement','sbml.py',692),
  ('if_statement -> IF LPAREN expression RPAREN block','if_statement',5,'p_if_statement','sbml.py',696),
  ('if_else_statement -> IF LPAREN expression RPAREN block ELSE block','if_else_statement',7,'p_if_else_statement','sbml.py',700),
  ('while_statement -> WHILE LPAREN expression RPAREN block','while_statement',5,'p_while_statement','sbml.py',704),
  ('empty_statement -> <empty>','empty_statement',0,'p_empty_statement','sbml.py',708),
  ('factor -> ID','factor',1,'p_expression_variable','sbml.py',713),
  ('list -> ID','list',1,'p_expression_variable','sbml.py',714),
  ('string -> ID','string',1,'p_expression_variable','sbml.py',715),
  ('tuple -> ID','tuple',1,'p_expression_variable','sbml.py',716),
  ('expression -> ID','expression',1,'p_expression_variable','sbml.py',717),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','sbml.py',722),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','sbml.py',727),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','sbml.py',728),
  ('expression -> term','expression',1,'p_expression_term','sbml.py',732),
  ('term -> term TIMES factor','term',3,'p_expression_binop1','sbml.py',736),
  ('term -> term DIVIDE factor','term',3,'p_expression_binop1','sbml.py',737),
  ('term -> factor POWER term','term',3,'p_expression_binop1','sbml.py',738),
  ('term -> term DIV factor','term',3,'p_expression_binop1','sbml.py',739),
  ('term -> term MOD factor','term',3,'p_expression_binop1','sbml.py',740),
  ('term -> factor','term',1,'p_term_factor','sbml.py',744),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_group','sbml.py',748),
  ('factor -> NUMBER','factor',1,'p_factor_number','sbml.py',752),
  ('factor -> MINUS factor','factor',2,'p_factor_uminus','sbml.py',756),
  ('expression -> string','expression',1,'p_expression_string','sbml.py',762),
  ('string -> STRING','string',1,'p_string_s','sbml.py',766),
  ('expression -> string PLUS expression','expression',3,'p_string_concatenation','sbml.py',771),
  ('expression -> string LBRACKET expression RBRACKET','expression',4,'p_string_index','sbml.py',776),
  ('expression -> list','expression',1,'p_expression_list','sbml.py',783),
  ('list -> LBRACKET tail','list',2,'p_list0','sbml.py',787),
  ('list -> LBRACKET expression tail','list',3,'p_list1','sbml.py',792),
  ('tail -> COMMA expression tail','tail',3,'p_list2','sbml.py',797),
  ('tail -> RBRACKET','tail',1,'p_tail','sbml.py',801),
  ('list -> list PLUS list','list',3,'p_list_concat','sbml.py',806),
  ('expression -> list LBRACKET expression RBRACKET','expression',4,'p_list_index0','sbml.py',811),
  ('list -> list LBRACKET expression RBRACKET','list',4,'p_list_index1','sbml.py',815),
  ('expression -> tuple','expression',1,'p_expression_tuple','sbml.py',821),
  ('tuple -> LPAREN expression tupletail','tuple',3,'p_tuple1','sbml.py',825),
  ('tupletail -> COMMA expression tupletail','tupletail',3,'p_tuple2','sbml.py',830),
  ('tupletail -> RPAREN','tupletail',1,'p_tupletail','sbml.py',834),
  ('expression -> TUPLEINDEX expression tuple','expression',3,'p_tuple_index0','sbml.py',838),
  ('tuple -> TUPLEINDEX expression tuple','tuple',3,'p_tuple_index1','sbml.py',842),
  ('boolean -> expression IN expression','boolean',3,'p_boolean_in','sbml.py',848),
  ('list -> expression CONCAT list','list',3,'p_expression_concat','sbml.py',854),
  ('boolean -> expression LT expression','boolean',3,'p_compare','sbml.py',860),
  ('boolean -> expression LE expression','boolean',3,'p_compare','sbml.py',861),
  ('boolean -> expression EQUALS expression','boolean',3,'p_compare','sbml.py',862),
  ('boolean -> expression NE expression','boolean',3,'p_compare','sbml.py',863),
  ('boolean -> expression GT expression','boolean',3,'p_compare','sbml.py',864),
  ('boolean -> expression GE expression','boolean',3,'p_compare','sbml.py',865),
  ('expression -> boolean','expression',1,'p_expression_boolean','sbml.py',871),
  ('boolean -> BOOLEAN','boolean',1,'p_boolean','sbml.py',875),
  ('expression -> NOT expression','expression',2,'p_boolean_not','sbml.py',879),
  ('expression -> expression AND expression','expression',3,'p_boolean_op','sbml.py',883),
  ('expression -> expression OR expression','expression',3,'p_boolean_op','sbml.py',884),
]
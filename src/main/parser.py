import ply.yacc as yacc
from lexer import tokens


precedence = (
    ('nonassoc', 'LE', 'GE', 'LT', 'GT', 'EQ', 'NE'),
    ('right', 'ASSIGN'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE')
)

# Gramática para el lenguaje    
def p_statements_expr(p):
    '''statement : expression'''
    p[0] = ('statement', p[1])

def p_statements_assign_binOP(p):
    '''statement : ID ASSIGN NUMBER SEMICOLON
                 | ID ASSIGN FLOAT SEMICOLON'''  
    p[0] = ('statement', p[1], p[3])
    
def p_statement_if_else(p):
    '''statement : IF LPAREN expression RPAREN LBRACE statement RBRACE ELSE LBRACE statement RBRACE'''
    p[0] = ('if', p[3], p[7], p[11])
    
#def p_statement_if_nobrace(p):
#    '''statement : IF LPAREN expression RPAREN statement SEMICOLON'''
#    p[0] = ('if', p[3], p[5])
    
#def p_statement_if(p):
#    '''statement : IF LPAREN expression RPAREN  LBRACE statement RBRACE'''
#    p[0] = ('if', p[3], p[6])

def p_statement_while(p):
    '''statement : WHILE LPAREN expression RPAREN LBRACE statement RBRACE'''
    p[0] = ('while', p[3], p[6])
    
def p_statement_do_while(p):
    ''' statement : DO LBRACE statement RBRACE  WHILE LPAREN expression RPAREN SEMICOLON'''
    p[0] = ('do while', p[3], p[6])

def p_statement_for(p):
    '''statement : FOR LPAREN statement expression RPAREN LBRACE statement RBRACE'''
    p[0] = ('for', p[3], p[4], p[7])
    
def p_statement_error(p):
    '''statement : error SEMICOLON'''
    print("ERROR: Error de statement. Mal Sintaxis")
    
def p_expression_error(p):
    '''expression : error SEMICOLON'''
    print("ERROR: Error de expresion. Mal Sintaxis")

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression MOD expression
                  '''
    p[0] = ('binop', p[1], p[2], p[3])

def p_expression_logical(p):
    ''' expression : expression LT expression
                   | expression LE expression
                   | expression GT expression
                   | expression GE expression
                   | expression EQ expression
                   | expression NE expression
    '''
    p[0] = ('logical', p[1], p[2], p[3])
    
def p_expression_group(p):
    '''expression : LPAREN expression RPAREN'''
    p[0] = ('grouped', p[2])

def p_expression_number(p):
    '''expression : NUMBER'''
    p[0] =  ('num', p[1])

def p_expression_float(p):
    '''expression : FLOAT'''
    p[0] =  ('float', p[1])

def p_expression_id(p):
    '''expression : ID'''
    p[0] =  ('id', p[1])

def p_expression_string(p):
    '''expression : STRING'''
    p[0] =  ('string', p[1])

def p_error(p):
        print("PANICO: Entrando en Estado de Panico! Descartando tokens de error")
        if not p:
            print("End of File!")
            return

        # Read ahead looking for a closing '}'
        while True:
            tok = parser.token()             # Get the next token
            if not tok or tok.type == 'RBRACE': 
                break
        parser.restart()
 # Construir el parser
parser = yacc.yacc()
     
def build_parser(input_string):        

    parser.parse(input_string, debug=True)




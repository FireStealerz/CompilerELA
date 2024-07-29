import ply.yacc as yacc
from lexer import tokens

# Gramática para el lenguaje
def p_program(p):
    '''program : statements'''
    p[0] = ('program', p[1])

def p_statements(p):
    '''statements : statements statement
                   | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement_expr(p):
    '''statement : expression SEMICOLON'''
    p[0] = ('expression', p[1])

def p_statement_assign(p):
    '''statement : ID ASSIGN expression SEMICOLON'''
    p[0] = ('assignment', p[1], p[3])

def p_statement_if(p):
    '''statement : IF LPAREN expression RPAREN LBRACE statements RBRACE ELSE LBRACE statements RBRACE'''
    p[0] = ('if', p[3], p[7], p[11])

def p_statement_while(p):
    '''statement : WHILE LPAREN expression RPAREN LBRACE statements RBRACE'''
    p[0] = ('while', p[3], p[6])

def p_statement_for(p):
    '''statement : FOR LPAREN ID ASSIGN expression SEMICOLON expression SEMICOLON expression RPAREN LBRACE statements RBRACE'''
    p[0] = ('for', p[3], p[5], p[7], p[9], p[12])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression MOD expression
                  | expression LT expression
                  | expression LE expression
                  | expression GT expression
                  | expression GE expression
                  | expression EQ expression
                  | expression NE expression'''
    p[0] = (p[2], p[1], p[3])

def p_expression_group(p):
    '''expression : LPAREN expression RPAREN'''
    p[0] = p[2]

def p_expression_number(p):
    '''expression : NUMBER'''
    p[0] = ('number', p[1])

def p_expression_float(p):
    '''expression : FLOAT'''
    p[0] = ('float', p[1])

def p_expression_id(p):
    '''expression : ID'''
    p[0] = ('id', p[1])

def p_expression_string(p):
    '''expression : STRING'''
    p[0] = ('string', p[1])

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

# Construir el parser
parser = yacc.yacc()

def parse(data):
    return parser.parse(data)

def print_parse_result(result, indent=0):
    """
    Imprime el resultado del análisis sintáctico de manera legible.
    """
    if isinstance(result, tuple):
        print('  ' * indent + str(result[0]))
        for item in result[1:]:
            print_parse_result(item, indent + 1)
    elif isinstance(result, list):
        for item in result:
            print_parse_result(item, indent)
    else:
        print('  ' * indent + str(result))

file = open("test2.txt")
saved_file = file.read() 
program = saved_file.split("\n")
program_string = ''.join(program)

result = parse(program_string)
print_parse_result(result)
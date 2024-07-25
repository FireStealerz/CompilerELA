#import ply.lex as lex
#import ply.yacc as yacc

'''
compiladorELA.py

Identificadores aceptados
var = variable
const = constante

palabras reservadas
var
const
int 
float
char
string

Tipos de datos
integer
float
char
string

Operadores Aritmeticos
+
+
*
/

Operadores Relacionales
<
>
<=
>=
==

Operadores Logicos
or
and
true
false

Caracteres especiales 
0
; 
{}
()

Sentencias Controladores
IF()
WHILE()
DO - WHILE()
FOR(int x; x <= 0; x++)
'''

reserved = {
    'var' : 'VAR',
    'const' : 'CONST',
    'int' : 'INT',
    'float' : 'FLOAT',
    'char' : 'CHAR',
    'string' : 'STRING',
    'true' : 'TRUE',
    'false' : 'FALSE',
    'if': 'IF',
    'while' : 'WHILE',
    'do' : 'DO',
    'for' : 'FOR',
    'print' : 'PRINT'
}

tokens = (
    #Operadores aritmeticos
    'SUM',
    'MINUS',
    'DIV',
    'MULT',
    #Operadores logicos
    'LESS',
    'LESSEQ',
    'EQ',
    'MORE',
    'MOREEQ',
    'OR',
    'AND',
    #Simbolos
    'PARIZQ',
    'PARDER',
    'CORIZQ',
    'CORDER',
    'SEMICOL',
    'DCOMILLA'
    #Asignar
    'ASIGN',
    #ID y tipos
    'ID',
    'NUM',
    'FLOATNUM',
    'STRINGTYPE'
    #Coment
    'COMMENT'
) + list(reserved.values())


t_SUM = r'\+'
t_MINUS = r'\-'
t_DIV = r'/'
t_MULT = r'\*'
t_LESS = r'<'
t_LESSEQ = r'<='
t_EQ = r'=='
t_MORE = r'>'
t_MOREEQ = r'>='
t_OR = r'\|{2}'
t_AND = r'\&\&'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\{'
t_CORDER = r'\}'
t_SEMICOL = r';'
t_ASIGN = r'='
t_DOBLECOMILLA = r'"'
t_ignore_COMMENT = r'#'
digit = 3

def t_ignore(t):
    r'\s'

def t_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value)
    
"""
Column Tracking for error handling
Input is the input string;
toke is a token instance 
def find_column(input, token):
    line_start = input.rfind('\#n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1
"""

def t_error(t):
    print("Illegal character or expresion %s in line %d, token no. %d" % t.value, t.lineno, t.lexpos)
    t.lexer.skip(1)
    

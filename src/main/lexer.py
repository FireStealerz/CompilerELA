import sys
import ply.lex as lex
from ply.lex import TOKEN


lex_pass = True;
# Palabras reservadas
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'do' : 'DO'
}
# Lista de tokens
tokens = [
    'ID', 'NUMBER', 'FLOAT', 'STRING',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN',
    'LBRACE', 'RBRACE',
    'ASSIGN',
    'SEMICOLON',
    'MOD',
    #'IF', 'ELSE', 'WHILE', 'FOR',
    'LT', 'LE', 'GT', 'GE', 'EQ', 'NE'
] + list(reserved.values())



# Reglas de expresión regular para tokens simples
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE  = r'\{'
t_RBRACE  = r'\}'
t_ASSIGN  = r'='
t_SEMICOLON = r';'
t_MOD     = r'%'
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='
t_EQ = r'=='
t_NE = r'!='
num_float = r'\d+\.\d+f'
num_int = r'\d+'
ID_RegEx = r'\$[a-z]+'
ID_Reserved = r'\b(if|else|while|for|do)\b'
string_type = r'\"([^\\\n]|(\\.))*?\"'

# Regla de expresión regular para números
@TOKEN(num_float)
def t_FLOAT(t):
    t.value = float(t.value[:-1])
    return t

@TOKEN(num_int)
def t_NUMBER(t):
    t.value = int(t.value)
    return t

# Regla de expresión regular para identificadores y palabras reservadas
@TOKEN(ID_RegEx)
def t_ID(t):
    t.type = reserved.get(t.value[1:], 'ID')    # Verifica si es una palabra reservada, omitiendo el símbolo $
    return t

# Regla de expresión regular para palabras reservadas
@TOKEN(ID_Reserved)
def t_RESERVED(t):
    t.type = reserved.get(t.value, 'ID')
    return t

# Regla de expresión regular para cadenas de texto
@TOKEN(string_type)
def t_STRING(t):    
    t.value = t.value[1:-1]  # Remover comillas dobles
    return t

# Regla de expresión regular para ignorar espacios y tabulaciones
t_ignore = ' \t'

# Regla de expresión regular para saltar líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores
def t_error(t):
    print(f"Caracter ilegal '{t.value[1]}' Posición: {t.lexpos}")
    print("\n\nEjecución finalizada ... \n\n\n")
    #t.lexer.skip(1)
    sys.exit(1)

def lex_main(test_file):

    # Construir el lexer
    lexer = lex.lex()

    # Prueba del lexer

    lexer.input(test_file)
    print("Ejecutando análisis léxico ... \n")
    for tok in lexer:
        print(tok)
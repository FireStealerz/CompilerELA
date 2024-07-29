import ply.lex as lex
from ply.lex import TOKEN

# Palabras reservadas
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR'
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

# Regla de expresión regular para números
@TOKEN(num_float)
def t_FLOAT(t):
    t.value = float(t.value[:-1])
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Regla de expresión regular para identificadores y palabras reservadas
def t_ID(t):
    r'\$[a-z]+'
    t.type = reserved.get(t.value[1:], 'ID')    # Verifica si es una palabra reservada, omitiendo el símbolo $
    return t

# Regla de expresión regular para palabras reservadas
def t_RESERVED(t):
    r'\b(if|else|while|for)\b'
    t.type = reserved.get(t.value, 'ID')
    return t

# Regla de expresión regular para cadenas de texto
def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
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
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

# Prueba del lexer
file = open("test.txt")
saved_file = file.read() 
program = saved_file.split("\n")
program_string = ''.join(program)

lexer.input(program_string)
fileWrite = open("testParser1.txt", "w") 

print("Primera Prueba: \n\n")
for tok in lexer:
    filew = str(tok)
    fileWrite.write(filew)
    print(tok)

fileWrite.close()
    
print("\n\nSegunda Prueba \n\n")

file = open("test2.txt")
saved_file = file.read() 
program = saved_file.split("\n")
program_string = ''.join(program)


lexer.input(program_string)

fileWrite = open("testParser2.txt", "w") 

for tok in lexer:
    filew = str(tok)
    fileWrite.write(filew)
    print(tok)

fileWrite.close()
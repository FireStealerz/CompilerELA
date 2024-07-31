import sys
from lexer import lex_main as lex


def lexic_analyzer():
    
    file = open("/home/ivanherran/Documents/Univa/Software de Sistemas/ProyectoCompilador/src/test/test.txt")
    saved_file = file.read() 
    program = saved_file.split("\n")
    program_string = ''.join(program)
      
    file_2 = open("/home/ivanherran/Documents/Univa/Software de Sistemas/ProyectoCompilador/src/test/test2.txt")
    saved_file = file_2.read() 
    program = saved_file.split("\n")
    program_string_2 = ''.join(program)

    lex(program_string, program_string_2)
    file.close()
    file_2.close()
    
lexic_analyzer()











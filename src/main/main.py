import sys
from dotenv import load_dotenv
import os
from lexer import lex_main as lex
from parser import build_parser as build_parser
from lexer import lex_pass as lex_check

def lexic_analyzer(file_path):
    
    file = open(file_path)
    saved_file = file.read() 
    program = saved_file.split("\n")
    program_string = ''.join(program)

    lex(program_string)
    file.close()

def parsing(file_path):
    
    file = open(file_path)
    saved_file = file.read() 
    program = saved_file.split("\n")
    program_string = ''.join(program)
    build_parser(program_string)
    file.close()
    

print("\n\nCompilando programa ... \n")
load_dotenv()
file_path = os.getenv('VICTOR_TESTING_FILE')    
lexic_analyzer(file_path)

if lex_check:
    parsing(file_path)











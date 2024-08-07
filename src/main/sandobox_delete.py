from dotenv import load_dotenv
import os

load_dotenv()

file_path = os.getenv('VICTOR_TESTING_FILE')

file = open(file_path)
saved_file = file.read() 
program = saved_file.split("\n")
program_string = ''.join(program)

print(program_string)

file.close()
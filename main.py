'''
se declara la funcion lexic_analyzer esta funcion será el analaziador lexico del compilador 
recibirá los parametros programa que es el codigo leído desde el archivo test.txt
y el parametro alplhabeto que es el el lenguaje que declaramos 
'''
def lexic_analayer(program, alphabet):

    count = 0  # la variable count es para obtener el número de línea
    error = False # para diagnosticar si existe un error en la compilación, en caso de que suceda un error cambia a True
    ela_alphabet = alphabet # simplemente se cambia el nombre de la variable

    # funcion try funciona para el manejo de errores
    try: 

        
        for line in program:  # este ciclo for funciona para leer renglon por renglon el programa
            count = count + 1 # la variable count es el número de linea que se esta analizando y se suma 1 en cada iteracion
            line_without_spaces = line.replace(" ", "") # se eliminan los espacios entre cada palabra
            tokens = [char for char in line_without_spaces] # se crea un arreglo de caracteres utilizando el texto sin espacios y se le da el nombre de tokens
            print("->Línea:", count, "Contenido:", tokens) # se imprime el número de linea correspondiente de la iteración y los tokens que contiene

            for token in tokens: # este ciclo for funciona para analizar el arreglo creado con los caracteres anteriomente y llamado tokens
                # print(token, "aceptado") if token in ela_alphabet else print(token, "rechazado")
                if token not in ela_alphabet:  # esta sentencia if funciona para revisar si el token pertenece a nuestro alfabeto
                    '''
                    en caso de que el token no pertenezca a nuestro alfabeto actualiza la variable error a true, imprimire los datos del error 
                    que es el token rechazado y la linea en la que esta el error
                    tambien detiene el programa
                    '''
                    error = True; 
                    print(f"\n--- Error léxico, el token '{token}', no pertenece al lenguaje de programación. Favor de revisar linea {count} ---")
                    print("--- Programa detenido ---")
                    break # detiene el programa
            if error: break # es un if en caso de que haya error detiene el programa
    except: # si existe un error no catalogado por el programa hace esta imprsesion en pantalla
        print("Ocurrio un error durante la compilación") # se imprime en caso de un error no catalogado
        



import string  # se importa la librería string 

file = open("test.txt") # se declara la variable file abriendo un archivo local de la computadora donde estara el codigo por analizar
saved_file = file.read() # se declara la variable save_file una vez que se leyó el contenido
program = saved_file.split("\n")  # se divide el programa en lineas 

letters = list(string.ascii_letters) # se declara la variable letters en base al codigo ascci contiene mayus y minus
numbers = list(string.digits) # se declara la varaible numbers contiene numeros del 0 al 9
symbols = ["+", "-", "*", "/", ">", "<", "=", ";", "{", "}", "(", ")", "'"] # se declara la variable symbols, contiene los simbolos del lenguaje creado
ela_alphabet = letters + numbers + symbols  # se declara la variable ela alphabet, la cual es un arreglo de letras, numeros y simbolos declarados anteriomente

'''
se llama a la funcion lexic analizaer la cual realizará el analisis lexico
se envía los parametros program creado anteriomente con un archivo local 
se envía el parametro ela_alphabet creado anteriomente en base a letras, números y simbolos
'''
lexic_analayer(program, ela_alphabet) # se llama la funcion lexic_analyzer con dos parametros












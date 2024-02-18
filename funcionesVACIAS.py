from configuracion import *
from principal import *
import math
import random


def unaAlAzar(abcd): #La funcion unaAlAzar debe elegir una letra al alazar de la lista abc del programa princial
    azar=random.choice(abcd) #Elige una letra al azar de la lista abc
    return(azar) #Devuelve esa letra

def esCorrecta(palabraUsuario, letra, item, items, listaDeTodo): # Esta funcion se encarga de retornar los puntajes
    if palabraUsuario[0]==letra: #se fija que la primer letra de la palabra del usuario sea igual a letra al azar
        i=0 # Inicializo la variable i que tomará los valores de la lista items en cada iteracion
        while i < len(items):# Mientras i sea menor a la longitud de la lista items
            if items[i]==item: # Se fija si la lista items en la posicion i es igual al item correspondiente
                if palabraUsuario in listaDeTodo[i]: # Si la palabra del usuario está en el item correcto
                    return(10) #Devuelve 10 puntos
                else:
                    return(0) # Sino devuelve 0 puntos
            i=i+1 # Aumento de variable para pasar al siguiente item
    else:
        return(-5) # Si la primer letra de la palabra del usuario no es igual a la letra al azar resta 5 puntos

def juegaCompu(letraAzar, listaDeTodo): # JuegaCompu retorna una lista con una palabra al azar de cada item que empieze con la letra al azar
    salida=[] # Es la lista donde se guardarán las palabras de cada item
    i=0 # Inicializo la valiable i que tomará los valores de la listaDeTodo en cada iteracion
    while i < len(listaDeTodo): # Mientras i sea menor a la longitud de la listaDeTodo
        palabra="" # Creo la variable palabra que por ahora esta vacia
        for elemento in listaDeTodo[i]: # La variable elemento tomará los valores que guarda cada item en cada una de las repeticiones
            if elemento[0]==letraAzar: # Si el elemento comienza con la letra estipulada
                palabra=elemento # La vaiable palabra toma el valor del elemento al que se la esta igualando
        salida.append(palabra)# agrega la palabra en la lista salida en caso de cumplir lo antetior o en caso de no tener palabra para algun item agrega una cadena vacia
        i=i+1 # Aumento la variable para pasar a la siguiente lista
    return(salida) #Devuelve la lista salida

def lectura(nombreArchivo): # La funcion lectura abre el archivo que tiene como parametro
    archivo=open(nombreArchivo+".txt","r") # Abrimos el archivo txt
    mostrar=[]
    elementos=archivo.readlines() # Elementos es una lista con todos valores del archivo
    for linea in elementos: # la variable linea toma cada valor que contiene elementos
        if linea[-1] == '\n': # verifica si hay un salto de linea
            linea = linea[:-1] # Borra el el salto de linea
            mostrar.append(linea) # Agrega a la lista mostrar cada valor
    archivo.close() # Cerramos el archivo
    return(mostrar) # Devuelve mostrar
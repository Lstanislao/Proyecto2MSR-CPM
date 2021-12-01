import os
import sys

def clearConsole():
    '''Funcion para limpiar la consola'''
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def header():
    clearConsole()
    print('________________________________________________________________________________________________________________')
    print()
    print('  ||||||||   |||||||      ||||||     ||    ||    ||||||||     |||||||    ||||||||     ||||||         ||||||||')
    print('  ||    ||   ||    ||    ||    ||    ||    ||    ||          ||    ||       ||       ||    ||              ||')
    print('  ||||||||   |||||||     ||    ||     ||||||     ||||||      ||             ||       ||    ||        ||||||||')
    print('  ||         ||    ||    ||    ||       ||       ||          ||             ||       ||    ||        ||     ')
    print('  ||         ||    ||    ||    ||       ||       ||          ||    ||       ||       ||    ||        ||     ')
    print('  ||         ||    ||     ||||||        ||       ||||||||     |||||||       ||        ||||||         ||||||||')
    print()
    print('________________________________________________________________________________________________________________')


def menu():
    print('\nPresione una de las siguientes opciones:\n')
    print('[1] Comenzar\n')
    print('[0] Cerrar programa\n')

graph = [["iZ1", "Nodo Origen", 0, ["-"]]]

def askNumber(query, greater, error, less):
    ''' Se pide el input hasta que sea un numero mayor al valor indicado '''
    valid = False
    while not valid:
        n = input(query)
        try: 
            if int(n) >= greater:
                if less == greater:
                    valid = True
                else:
                    if int(n) <= less:
                        valid = True
                    else:
                        valid = False
                        print(error)
            else:
                valid = False
                print(error)
        except:
            valid = False
            print(error)

    return int(n)

def activities():
    ''' Se piden todas las actividades con su respectiva informacion '''

    # Se pide el numero de actividades hasta que se haya ingresado un numero mayor o igual a 2
    quantity = askNumber('\nIngrese la cantidad de actividades que tendrá el grafo: ', 2, '\nDebe ingresar un numero mayor o igual a 2. Por favor, intente de nuevo', 2)
  
    print('\nAhora hay que agregar todas las actividades. Solo podras agregar actividades cuyas actividades predecesoras ya hayan sido agregadas.\n')

    for i in range(int(quantity)):
        activity()

    contadorFP = 0
    print('\n\n¡Su grafo esta listo!\n')
    for i in range(len(graph)):
        if (i != 0):
            if graph[i][3] == ['iZ1']:
                contadorFP += 1
            print(graph[i])
    print('\n\n')
    return [graph, contadorFP]

def activity():
    ''' Se pide una actividad con su identificador, descripcion, duracion y predecesores '''

    valid = False
   
   # Se pide el identificador de la actividad hasta que sea uno repetido
    while not valid:
        id = input('\nIngrese el identificador de la nueva actividad actividad. (Por ejemplo: "A", "b", "C", "1", "II", "3"\n')

        valid = True
        for a in graph:
            if a[0] == id:
                valid = False
                print('\nEse identificador ya esta registrado, debe escoger uno diferente. Por favor, intente de nuevo')

    # Se pide la descripcion de la actividad
    description = input('\nIngrese la descripcion de la actividad. (Por ejemplo: "Limpiar ventanas", "Llevar el carro al taller", "Mezclar el azucar con los huevos"\n')
    
    # TODO: no se si poner >= 0 0 >= 1
    value = askNumber('\nIngrese la duracion de la actividad: ', 1, '\nDebe ingresar un numero mayor o igual a 1. Por favor, intente de nuevo', 1)

    act = [id, description, int(value)]

    # Se escogen los predecesores
    predecesor = []
    print('\n\nAhora hay que especificar los predecesores de la actividad.\n')
    # Si es la primera actividad que se esta agregando no tiene predecesores
    if len(graph) - 1 == 0:
        # print('Esta es la primera actividad que estas agregando, asi que no tendra predecesor.\n')
        predecesor.append("iZ1")
        act.append(predecesor)
        
    # De lo contrario se pregunta el numero de predecesores hasta que ingrese un numero entre 1 y num de actividades registradas
    else:
        count = askNumber('\n¿Cuántos predecesores tiene esta actividad?\nIngrese 0 si no posee predecesor. Solo hay {0} actividad(es) registrada(s)\n'.format(len(graph) - 1),
                        0,
                        '\nLa actividad debe tener un numero minimo de 0 y maximo {0} predecesor(es). Por favor, intente de nuevo'.format(len(graph) - 1), 
                        len(graph) - 1)
        
        if (count == 0):
            predecesor.append("iZ1")
            act.append(predecesor)
        else:

            # Se buscan los posibles predecesores
            preArray = []
            for x in graph:
                if x[0] != 'iZ1':
                    preArray.append(x[0])

            # Se piden los n predecesores indicados pidiendo su identificador
            for i in range(count):
                valid = False

                # Mientras no se ingrese un identificador disponible (registrado y no repetido), se repite
                while not valid:
                    clearConsole()
                    print('Ingrese el identificador que precede a esta actividad:\n')
                    print('Identificadores disponibles:\n')
                    print(preArray)
                    print('')
                    predecesorInput = input('\n')
                    
                    if (predecesorInput not in preArray):
                        print('\nEl identificador ingresado no esta entre las opciones posibles, por favor, intente de nuevo.\n')
                        valid = False
                    else:
                        valid = True
                        preArray.remove(predecesorInput)
                
                predecesor.append(predecesorInput)

            act.append(predecesor)
    clearConsole()
    if len(graph) - 1 == 0:
        print('Esta es la primera actividad que estas agregando, asi que no tendra predecesor.\n')
    if (act[3] == ['iZ1']):
        aux = []
        for x in act:
            aux.append(x)
        aux[3] = ['-']
        print('Actividad:', aux)
    else:
        print('Actividad:', act)

    # Se agrega la actividad
    graph.append(act)
    print("\nSe ha registrado la actividad.")

    
def credits():
    print('\nProyecto 2 - Modelación de Sistemas en Redes')
    print('Profesor:')
    print('     -> Rafael Matienzo')
    print('\nIntegrantes:')
    print('     -> Oriana González')
    print('     -> Guillermo Sosa')
    print('     -> Luis Stanislao')
    print('\nProyecto 2 finalizado\n')
    sys.exit(0)


# header()
# menu()
# start = input('\n')
# clearConsole()
# if start == '1':
#     activities()
# elif start == '0':
#     credits()
# else:
#    print('\n La opción ingresada no es válida, por favor, intente de nuevo \n')
#    menu()
#    start = input('\n') 

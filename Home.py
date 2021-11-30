def header():
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

graph = []

def activities():
    quantity = input('\nIngrese la cantidad de actividades que tendrá el grafo:')
    for i in range(int(quantity)):
        activity()
    print(graph)

def activity():
    id = input('\nIngrese el identificador de la actividad. (Por ejemplo: "A", "b", "C", "1", "II", "3"\n')
    description = input('Ingrese la descripcion de la actividad. (Por ejemplo: "Limpiar ventanas", "Llevar el carro al taller", "Mezclar el azucar con los huevos"\n')
    value = input('Ingrese el valor de la actividad.\n')
    act = [id, description, int(value)]
    predecesor = []
    pre = input('¿Esta actividad tiene predecesor? \nIngrese una de las siguientes opciones:  \n[1] SI\n[0] NO\n')

    if pre == '1':
        count = int(input('¿Cuántos predecesores tiene esta actividad?\n'))
        while count < 0:
            count = int(input('¿Cuántos predecesores tiene esta actividad?\n'))

        preArray = []
        for x in graph:
                preArray.append(x[0])

        for i in range(count):
            print('Ingrese el identificador que precede a esta actividad:\n')
            print('Identificadores disponibles:\n')
            print(preArray)
            print('')
            predecesorInput = input('\n')

            while predecesorInput not in preArray:
                print('Ingrese el identificador que precede a esta actividad:\n')
                print('Identificadores disponibles:\n')
                print(preArray)
                print('')
                predecesorInput = input('\n')
                
                if (predecesorInput not in preArray):
                    print('\nEl identificador ingresado no está registrado, por favor, intente de nuevo.\n')
            
            predecesor.append(predecesorInput)

        act.append(predecesor)

    elif pre == '0':
        predecesor.append("-")
        act.append(predecesor)
    else:
        print("La opción ingresada no es válida, por favor, intente de nuevo\n")
        pre = input('¿Esta actividad tiene predecesor? \nIngrese una de las siguientes opciones:  \n[1] SI\n[0] NO\n')

    print(act)
    graph.append(act)
    
def credits():
    print('\nProyecto 2 - Modelación de Sistemas en Redes')
    print('Profesor:')
    print('     -> Rafael Matienzo')
    print('\nIntegrantes:')
    print('     -> Oriana González')
    print('     -> Guillermo Sosa')
    print('     -> Luis Stanislao')
    print('\nProyecto 2 finalizado\n')


header()
menu()
start = input('\n')
if start == '1':
    activities()
elif start == '0':
    credits()
else:
   print('\n La opción ingresada no es válida, por favor, intente de nuevo \n')
   menu()
   start = input('\n') 

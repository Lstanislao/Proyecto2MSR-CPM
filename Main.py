
import sys
import os
import time
from prettytable import PrettyTable
from pyfiglet import Figlet

from CPM import CPM
from Home import header, menu, activities, credits, askNumber


def clearConsole():
    '''Funcion para limpiar la consola'''
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

if __name__ == '__main__':

    header()
    menu()
    start = input('\n')
    clearConsole()
    if start == '1':
        mainArray = activities()[0]

        project = CPM(mainArray)
        # project = CPM([['iZ1', 'Nodo Origen', 0, ['-']], ['a', 'dd', 3, ['iZ1']], ['b', 'ff', 4, ['a']], ['c', 'ff', 2, ['a']], ['d', 'ee', 5, ['b']], ['e', 'dd', 1, ['c']], ['f', 'ff', 2, ['c']], ['g', 'ff', 4, ['d', 'e']], ['h', 'dd', 3, ['f', 'g']], ['jA2', 'Nodo Final', 0, ['h']]])
        # project = CPM([['iZ1', 'Nodo Origen', 0, ['-']], ['a', 'gg', 2, ['iZ1']], ['b', 'jj', 3, ['a']], ['e', 'rr', 5, ['a']], ['c', 'hh', 1, ['b', 'e']], ['d', 'uu', 3, ['e']], ['f', 'gg', 2, ['c', 'd']], ['g', 'ff', 2, ['f']], ['fz1', 'ff', 0, ['g']]])
        # project = CPM([['iZ1', 'Nodo Origen', 0, ['-']], ['a', 'gg', 2, ['iZ1']], ['b', 'jj', 5, ['iZ1']], ['c', 'hh', 4, ['a']], ['d', 'uu', 6, ['b', 'c']], ['e', 'rr', 3, ['d']], ['f', 'gg', 8, ['e']], ['g', 'ff', 10, ['e']], ['fz1', 'ff', 0, ['f', 'g']]])
        results = project.calculateCPM()

        # Se construye la tabla de resultados despues del forward y backward pass con los dias
        # mas tempranos y tardios de inicio y fin
        finalTable = PrettyTable()
        finalTable.field_names = ["ID",
                                "Description", "Duration", "Early Start", "Early Finish", "Late Start", "Late Finish"]

        # Se construye la tabla de resultados de las holguras de las actividades
        slackTable = PrettyTable()
        slackTable.field_names = ["ID",
                                "Slack"]

        # Se agregan a las tablas los resultados calculados
        slackTable.add_rows(results['slacks'])
        finalTable.add_rows(results['finalTable'])

        # Se muestra la tabla con los dias mas tempranos y tardios de inicio y fin de
        # las actividades
        print(finalTable)

        # Se muestran las actividades de la ruta critica
        s = results['slacks']
        a = ""
        for i in range(len(s)):
            if s[i][1] == 0:
                if a == '':
                    a += s[i][0]
                else:
                    a += ', ' + s[i][0]

        print("\nLas actividades de la ruta critica son: {0}\n".format(a))

        # Se muestran las actividades con su respectiva holgura
        print(slackTable)
        print('\n\n')
        credits()
    elif start == '0':
        credits()

    else:
        clearConsole()
        header()
        print('\n La opción ingresada no es válida, por favor, intente de nuevo \n')
        menu()
        start = input('\n')

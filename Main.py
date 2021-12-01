
import sys
import os
import time
from prettytable import PrettyTable
from pyfiglet import Figlet

from CPM import CPM
from Home import header, menu, activities, credits


def clearConsole():
    '''Funcion para limpiar la consola'''
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


# tablas de ejemplo igual a las del parcial
# la primera posicion de cada array es un indentificador con el cual se refiere en las otras tablas
# TODO: CUANDO VAYAN A PEDIR ESTO QUE ES EL INPUT DEL METODO CONSIDERE QUE PUEDEN HABER 2 PRIMERAS ACTIVIDADES
# Y COLOCAR "-" CUANTO NO TENGA REQUISITO O PREDECESOR UNA ACTIVIDAD
main = [["A", "yolo", 2, ["-"]],
        ["B", "yolo", 3, ["A"]],
        ["C", "yolo", 1, ["B", "E"]],
        ["D", "yolo", 3, ["E"]],
        ["E", "yolo", 5, ['A']],
        ["F", "yolo", 2, ['C', 'D']],
        ["G", "yolo", 2, ['F']],
         ]


if __name__ == '__main__':


    header()
    menu()
    start = input('\n')
    clearConsole()
    if start == '1':
        mainArray = activities()[0]
        print('\n\nMiraAca\n')
        print(mainArray)
        print('\n\n')

        project = CPM(mainArray)
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

        # TODO: mostrar ruta critica

        # Se muestran las actividades con su respectiva holgura
        print(slackTable)       
    
    
    elif start == '0':
        credits()
    
    
    else:
        clearConsole()
        header()
        print('\n La opción ingresada no es válida, por favor, intente de nuevo \n')
        menu()
        start = input('\n') 


    # project = CPM(main)
    # results = project.calculateCPM()

    # # Se construye la tabla de resultados despues del forward y backward pass con los dias
    # # mas tempranos y tardios de inicio y fin
    # finalTable = PrettyTable()
    # finalTable.field_names = ["ID",
    #                           "Description", "Duration", "Early Start", "Early Finish", "Late Start", "Late Finish"]
    
    # # Se construye la tabla de resultados de las holguras de las actividades
    # slackTable = PrettyTable()
    # slackTable.field_names = ["ID",
    #                           "Slack"]

    # # Se agregan a las tablas los resultados calculados
    # slackTable.add_rows(results['slacks'])
    # finalTable.add_rows(results['finalTable'])

    # # Se muestra la tabla con los dias mas tempranos y tardios de inicio y fin de 
    # # las actividades
    # print(finalTable)

    # # TODO: mostrar ruta critica

    # # Se muestran las actividades con su respectiva holgura
    # print(slackTable)

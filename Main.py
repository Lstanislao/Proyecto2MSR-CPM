
import sys
import os
import time
from prettytable import PrettyTable
from pyfiglet import Figlet

from CPM import CPM


def clearConsole():
    '''Funcion para limpiar la consola'''
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


# tablas de ejemplo igual a las del parcial
# la primera posicion de cada array es un indentificador con el cual se refiere en las otras tablas
#CUANDO VAYAN A PEDIR ESTO QUE ES EL INPUT DEL METODO CONSIDERE QUE PUEDEN HABER 2 PRIMERAS ACTIVIDADES
# Y COLOCAR "-" CUANTO NO TENGA REQUISITO O PREDECESOR UNA ACTIVIDAD
main = [["A", "yolo", 2, ["-"]],
        ["B", "yolo", 3, ["A"]],
        ["C", "yolo", 1, ["B", "E"]],
        ["D", "yolo", 3, ["E"]],
        ["E", "yolo", 5, ['A']],
        ["F", "yolo", 2, ['C', 'D']],
        ["G", "yolo", 2, ['F']], ]


if __name__ == '__main__':
    project = CPM(main)
    results = project.calculateCPM()
    finalTable = PrettyTable()
    finalTable.field_names = ["ID",
                              "Description", "Duration", "Early Start", "Early Finish", "Late Start", "Late Finish"]
    slackTable = PrettyTable()
    slackTable.field_names = ["ID",
                              "Slack"]

    slackTable.add_rows(results['slacks'])
    finalTable.add_rows(results['finalTable'])

    print(finalTable)
    print(slackTable)

sys.exit(0)


class CPM:
    # matriz para el forward
    adjMatrixForward = []
    # matrix para el backward
    adjMatrixBackward = []
    # tabla resultante despues de las forw y el backw
    finalMatrix = []
    # tabla de la actividades que viene por input para armar CP
    activitiesTable = []
    # diccionario que enelaza cada letra con un numeropara hacer una especie de indexing
    activities = {}

    def __init__(self, activitiesTable):
        # se guardan las activdades como atributo del objeto para accesarla desde cualquier metodo
        self.activitiesTable = activitiesTable

        # se incializa la matriz final (ES, EF, LS, LF)
        for i in range(len(activitiesTable)):
            self.finalMatrix.append([0, 0, 999, 999])

        # diccionario para obtener las key de cada actividad(es como una especie de indexing)
        # para obtener rapidamente el index de determinada letra
        cont = 0
        for key in activitiesTable:
            self.activities[key[0]] = cont
            cont += 1

        # se inicializa la matriz para forward (es una matriz de adj)
        for i in range(len(self.activitiesTable)):
            self.adjMatrixForward.append([0]*len(self.activitiesTable))

        # se llena la matriz del forward
        for i in range(len(self.activitiesTable)):
            # Se verifica que no sea la primera actividad
            if self.activitiesTable[i][3][0] != '-':
                # Si es la ultima actividad se marca la interseccion con ese mismo nodo es decir [G][G]
                # para que haga la condicion de parada en el forward pass , de esta manera sabemos que hasta ahi llega el grafo
                if i == (len(self.activitiesTable)-1):
                    self.adjMatrixForward[i][i] = self.activitiesTable[i][2]
                # Es una matriz de adj por lo tanto para hacer B primero tengo que hacer A
                # entonces la distancia o el arco entre A y B tiene como peso la duracion de A,
                # pues es lo necesario para llegar a B
                # entonces aqui va por cada requisito llenando esa interseccion
                for j in self.activitiesTable[i][3]:
                    self.adjMatrixForward[self.activities[j]
                                          ][i] = self.activitiesTable[self.activities[j]][2]

        # se inicializa la matriz para el backward
        for i in range(len(self.activitiesTable)):
            self.adjMatrixBackward.append([0]*len(self.activitiesTable))
        # se llena la matrix para backward, simililar a la del foward
        for i in range(len(self.activitiesTable)):
            # como se viene del final hacia a atras se marca la primera como fin del grafo
            if i == 0:
                self.adjMatrixBackward[i][i] = self.activitiesTable[i][2]
            # si la actividad tiene requisito o precesor
            if self.activitiesTable[i][3][0] != '-':
                # verificar si es la actividad final
                if i == 0:
                    # se marca la actividad final
                    self.adjMatrixBackward[i][i] = self.activitiesTable[i][2]

                # se guarda la duracion entre cada actividad
                for j in self.activitiesTable[i][3]:
                    self.adjMatrixBackward[i][self.activities[j]
                                              ] = self.activitiesTable[self.activities[j]][2]

    def forwardPass(self):
        # queue pa bfs
        queue = []
        # vector booleano
        visited = [False]*len(self.adjMatrixForward)
        # flag de la condicion de parada
        stop = False
        # auxiliar para recorrer el grafo
        aux = 1
        # forward pass
        # la condicion de parada es que haya llegado al ultimo nodo o actividad
        # que lo marcamos en la iniclizacion
        while stop == False:
            # si hay alguien en la cola desapilo
            if queue:
                aux = queue.pop(0)
            #print('visito: '+str(aux))
            currentTime = 0
            # se recorre la fila del nodo actual, para identificar sus sucesores
            for h in range(len(self.adjMatrixForward[aux-1])):
                if self.adjMatrixForward[aux-1][h] != 0:
                    # en caso que sea el primer nodo sabemos EF y ES
                    if aux == 1:
                        # ES 0
                        self.finalMatrix[aux-1][0] = 0
                        # EF la duracion
                        self.finalMatrix[aux -
                                         1][1] = self.adjMatrixForward[aux-1][h]

                    # se guarda la duracion de la actividad en current time
                    else:
                        currentTime = self.adjMatrixForward[aux-1][h]
                    # se marca el nodo como visitado
                    visited[aux-1] = True
                    # se agregan a la queue los hijos del nodo actual
                    if visited[h] == False and h+1 not in queue:
                        queue.append(h+1)

        # se vuelve a recorrer la fila para guardar EF y ES de sus predecesoras
            for i in range(len(self.adjMatrixForward[aux-1])):
                # si el valor en la matriz de adyacencia en esa posición es distinto de cero (significa que la actividad es predecesora de la actual)
                if self.adjMatrixForward[i][aux-1] != 0 and i != aux-1:
                    # si el valor del nodo actual es distinto de 1
                    if aux != 1:
                        # si el valor EF en la matriz fechas de la posición actual es mayor al guardado del ES en la matriz fechas para el nodo actual
                        if self.finalMatrix[i][1] > self.finalMatrix[aux-1][0]:
                            # se guarda el valor como ES en la matriz fechas para el nodo actual
                            self.finalMatrix[aux-1][0] = self.finalMatrix[i][1]
                        # si el valor ES en la matriz fechas para la posicón actual + el tiempo actual guardado anteriormente es mayor al EF guardado del nodo actual
                        if self.finalMatrix[i][1] + currentTime > self.finalMatrix[aux-1][1]:
                            # se guarda el valor como EF en la matriz fechas para el nodo actual
                            self.finalMatrix[aux -
                                             1][1] = self.finalMatrix[i][1] + currentTime
            #print('queue: '+str(queue))
            if False not in visited:
                stop = True

        # queue pa bfs
        queue = []
        # vector booleano
        visited = [False]*len(self.adjMatrixForward)
        # flag de la condicion de parada
        stop = False
        # auxiliar para recorrer el grafo
        aux = 1
        # forward pass
        # la condicion de parada es que haya llegado al ultimo nodo o actividad
        # que lo marcamos en la iniclizacion
        while stop == False:
            # si hay alguien en la cola desapilo
            if queue:
                aux = queue.pop(0)
            #print('visito: '+str(aux))
            currentTime = 0
            # se recorre la fila del nodo actual, para identificar sus sucesores es decir hacer el BFS
            for h in range(len(self.adjMatrixForward[aux-1])):
                if self.adjMatrixForward[aux-1][h] != 0:
                    # en caso que sea el primer nodo sabemos EF y ES
                    if aux == 1:
                        # ES 0
                        self.finalMatrix[aux-1][0] = 0
                        # EF la duracion
                        self.finalMatrix[aux -
                                         1][1] = self.adjMatrixForward[aux-1][h]

                    # se guarda la duracion de la actividad en current time
                    else:
                        currentTime = self.adjMatrixForward[aux-1][h]
                    # se marca el nodo como visitado
                    visited[aux-1] = True
                    # se agregan a la queue los hijos del nodo actual
                    if visited[h] == False and h+1 not in queue:
                        queue.append(h+1)

        # se vuelve a recorrer la fila para guardar EF y ES de sus sucesoras
            for i in range(len(self.adjMatrixForward[aux-1])):
                # si el valor en la matriz de adyacencia en esa posición es distinto de cero (significa que la actividad es sucesora de la actual)
                if self.adjMatrixForward[i][aux-1] != 0 and i != aux-1:
                    # si el valor del nodo actual es distinto de 1
                    # estas operaciones son para las activdades sucesoras al nodo actual
                    if aux != 1:
                        # Si el EF de la actual es mayor que es ES de la sucesora se actualiza el ES
                        if self.finalMatrix[i][1] > self.finalMatrix[aux-1][0]:
                            # se guarda el valor como ES en la matriz fechas para el nodo actual
                            self.finalMatrix[aux-1][0] = self.finalMatrix[i][1]
                        # Si el EF actual es menor que el ES + la duracion se actualiza el EF
                        if self.finalMatrix[i][1] + currentTime > self.finalMatrix[aux-1][1]:
                            # se guarda el valor como EF en la matriz fechas para el nodo actual
                            self.finalMatrix[aux -
                                             1][1] = self.finalMatrix[i][1] + currentTime
            # condicion de parada
            if False not in visited:
                stop = True

    def backwardPass(self):
        # queue pa bfs
        queue = []
        # vector booleano
        visited = [False]*len(self.adjMatrixBackward)
        # flag de la condicion de parada
        stop = False
        # aux para recorrer el grafo
        aux = len(self.activitiesTable)

        while stop == False:
            # si hay alguien en la cola desapilo
            if queue:
                aux = queue.pop(0)
            #print('visito: '+str(aux))
            # Se realiza el recorrido BFS pero de atras hacia adelante
            for h in range(len(self.adjMatrixBackward[aux-1])):
                if self.adjMatrixBackward[aux-1][h] != 0:
                    # se setea el LS y EF del ultimo nodo que es igual a su ES y EF
                    if aux == len(self.activitiesTable):
                        self.finalMatrix[aux-1][2] = self.finalMatrix[aux-1][0]
                        self.finalMatrix[aux-1][3] = self.finalMatrix[aux-1][1]
                    # se marca como visitado en el vector booleano
                    visited[aux-1] = True
                    # se agregan a la queue los hijos del nodo actual, ccumpliendo con el bfs
                    if visited[h] == False and h+1 not in queue:
                        queue.append(h+1)
            # se recorre la fila para guardar LS y LF de cada actividad predecesora en este caso
            for i in range(len(self.adjMatrixForward[aux-1])):
                # si la matriz en esa posicion tiene valor es porque esa actividad es precesora
                if self.adjMatrixForward[aux-1][i] != 0 and i != aux-1:
                    # si el nodo no es el último
                    if aux != len(self.activitiesTable):
                        # si el LF guardado actualmente  en la matriz final es menor que LS  se actualiza
                        if self.finalMatrix[i][2] < self.finalMatrix[aux-1][3] or self.finalMatrix[i][2] < self.finalMatrix[aux-1][2]:
                            # se guarda el valor como LF en la matriz final  para este nodo
                            self.finalMatrix[aux-1][3] = self.finalMatrix[i][2]
                        #se actualiza LS si es menor que la LF menos la duracion en el nodo actual
                        if self.finalMatrix[i][2] - self.adjMatrixForward[aux-1][i] < self.finalMatrix[aux-1][2]:
                            # se guarda el valor como LS en la matriz final  para el nodo actual
                            self.finalMatrix[aux-1][2] = self.finalMatrix[i][2] - \
                                self.adjMatrixForward[aux-1][i]
            #print('queue: '+str(queue))
            # si todos los nodos han sido visited se termina el ciclo
            if False not in visited:
                stop = True

    def calculateCPM(self):
      #paso hacia adelante
        self.forwardPass()
      #paso hacia atras
        self.backwardPass()
      #holguras
        slacks = []
        for i in range(len(self.activitiesTable)):
            slack = self.finalMatrix[i][2] - self.finalMatrix[i][0]
            slacks.append([slack])
      #dandole formato a la matriz final
        for i in range(len(self.finalMatrix)):
            self.finalMatrix[i].insert(0, self.activitiesTable[i][2])
            self.finalMatrix[i].insert(0, self.activitiesTable[i][1])
            self.finalMatrix[i].insert(0, self.activitiesTable[i][0])

            slacks[i].insert(0, self.activitiesTable[i][0])

        return {'finalTable': self.finalMatrix, "slacks": slacks}

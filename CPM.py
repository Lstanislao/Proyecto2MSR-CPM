
class CPM:
    # Matriz para el forward
    adjMatrixForward = []
    # Matriz para el backward
    adjMatrixBackward = []
    # Tabla resultante despues del forward y el backward pass
    finalMatrix = []
    # Tabla de la actividades que viene como argumento para calcular la ruta critica
    activitiesTable = []
    # Diccionario que enlaza cada letra con un numero para hacer una especie de indexing
    activities = {}

    def __init__(self, activitiesTable):
        # Se guardan las actividades como atributo del objeto para acceder a ellas desde cualquier metodo
        self.activitiesTable = activitiesTable

        # Se incializa la matriz final (ES, EF, LS, LF)
        for i in range(len(activitiesTable)):
            self.finalMatrix.append([0, 0, 999, 999])

        # Se construye el diccionario para obtener las key de cada actividad(es como una especie de indexing)
        # para obtener rapidamente el index de determinada letra
        cont = 0
        for key in activitiesTable:
            self.activities[key[0]] = cont
            cont += 1

        # Se inicializa la matriz para el forward pass (es una matriz de adj)
        for i in range(len(self.activitiesTable)):
            self.adjMatrixForward.append([0]*len(self.activitiesTable))

        # Se llena la matriz haciendo el forward pass
        for i in range(len(self.activitiesTable)):
            # Se verifica que no sea la primera actividad
            if self.activitiesTable[i][3][0] != '-':

                # Si es la ultima actividad se marca la interseccion con ese mismo nodo es decir [i][i]
                # para que haga la condicion de parada en el forward pass, de esta manera sabemos que hasta ahi llega el grafo
                if i == (len(self.activitiesTable)-1):
                    self.adjMatrixForward[i][i] = self.activitiesTable[i][2]

                # Es una matriz de adj por lo tanto para hacer B primero tengo que hacer A,
                # entonces la distancia o el arco entre A y B tiene como peso la duracion de A,
                # pues es lo necesario para llegar a B. 

                # Aqui va por cada requisito para empezar la actividad llenando esa interseccion
                for j in self.activitiesTable[i][3]:
                    self.adjMatrixForward[self.activities[j]
                                          ][i] = self.activitiesTable[self.activities[j]][2]

        # Se inicializa la matriz para el backward pass
        for i in range(len(self.activitiesTable)):
            self.adjMatrixBackward.append([0]*len(self.activitiesTable))

        # Se llena la matriz para backward, simililar a la del foward
        for i in range(len(self.activitiesTable)):
            # Como se viene del final hacia atras se marca la primera como fin del grafo
            if i == 0:
                self.adjMatrixBackward[i][i] = self.activitiesTable[i][2]
            # Si la actividad tiene requisito o predecesor
            if self.activitiesTable[i][3][0] != '-':
                # Se verifica si es la actividad final
                if i == 0:
                    # Se marca la actividad final
                    self.adjMatrixBackward[i][i] = self.activitiesTable[i][2]

                # se guarda la duracion entre cada actividad
                for j in self.activitiesTable[i][3]:
                    self.adjMatrixBackward[i][self.activities[j]
                                              ] = self.activitiesTable[self.activities[j]][2]

    def forwardPass(self):
        ''' Se hace el forward pass que consiste en calcular para cada actividad el early start 
        y early finish '''

        # Cola para aplicar bfs
        queue = []
        # Vector booleano para indicar los nodos visitados
        visited = [False]*len(self.adjMatrixForward)
        # Flag de la condicion de parada
        stop = False
        # Auxiliar para recorrer el grafo
        aux = 1

        # la condicion de parada es que haya llegado al ultimo nodo o actividad
        # que lo marcamos en la inicializacion
        while stop == False:
            # Si hay alguien en la cola desencolo
            if queue:
                aux = queue.pop(0)

            currentTime = 0
            # Se recorre la fila del nodo actual, para identificar sus sucesores
            for h in range(len(self.adjMatrixForward[aux-1])):
                if self.adjMatrixForward[aux-1][h] != 0:
                    # En caso que sea el primer nodo sabemos EF y ES
                    if aux == 1:
                        # ES es 0
                        self.finalMatrix[aux-1][0] = 0
                        # EF es la duracion
                        self.finalMatrix[aux -
                                         1][1] = self.adjMatrixForward[aux-1][h]

                    # Se guarda la duracion de la actividad en current time
                    else:
                        currentTime = self.adjMatrixForward[aux-1][h]
                    # Se marca el nodo como visitado
                    visited[aux-1] = True
                    # Se agregan a la cola los hijos del nodo actual
                    if visited[h] == False and h+1 not in queue:
                        queue.append(h+1)

        # Se vuelve a recorrer la fila para guardar EF y ES de sus predecesores
            for i in range(len(self.adjMatrixForward[aux-1])):
                # Si la actividad es predecesora de la actividad actual
                if self.adjMatrixForward[i][aux-1] != 0 and i != aux-1:
                    # Si el valor del nodo actual no es 1
                    if aux != 1:
                        # Si el EF de la posicion actual es mayor que el ES del sucesor se actualiza el ES
                        if self.finalMatrix[i][1] > self.finalMatrix[aux-1][0]:
                            # Se guarda el valor como ES en la matriz final para el nodo actual
                            self.finalMatrix[aux-1][0] = self.finalMatrix[i][1]
                        # Si el EF actual es menor que el ES + la duracion se actualiza el EF
                        if self.finalMatrix[i][1] + currentTime > self.finalMatrix[aux-1][1]:
                            # Se guarda el valor como EF en la matriz final para el nodo actual
                            self.finalMatrix[aux -
                                             1][1] = self.finalMatrix[i][1] + currentTime

            if False not in visited:
                stop = True

    def backwardPass(self):
        # Cola pa bfs
        queue = []
        # Vector booleano para marcar nodos visitados
        visited = [False]*len(self.adjMatrixBackward)
        # Flag de la condicion de parada
        stop = False
        # Auxiliar para recorrer el grafo
        aux = len(self.activitiesTable)

        while stop == False:
            # si hay alguien en la cola desencolo
            if queue:
                aux = queue.pop(0)

            # Se realiza el recorrido BFS pero de atras hacia adelante
            for h in range(len(self.adjMatrixBackward[aux-1])):
                if self.adjMatrixBackward[aux-1][h] != 0:
                    # Se setea el LS y EF del ultimo nodo que es igual a su ES y EF
                    if aux == len(self.activitiesTable):
                        self.finalMatrix[aux-1][2] = self.finalMatrix[aux-1][0]
                        self.finalMatrix[aux-1][3] = self.finalMatrix[aux-1][1]
                    # Se marca como visitado en el vector booleano
                    visited[aux-1] = True
                    # Se agregan a la cola los hijos del nodo actual, cumpliendo con el bfs
                    if visited[h] == False and h+1 not in queue:
                        queue.append(h+1)

            # Se recorre la fila para guardar LS y LF de cada actividad predecesora en este caso
            for i in range(len(self.adjMatrixForward[aux-1])):
                # Si la matriz en esa posicion tiene valor es porque esa actividad es predecesora
                if self.adjMatrixForward[aux-1][i] != 0 and i != aux-1:
                    # Si el nodo no es el último
                    if aux != len(self.activitiesTable):
                        # Si el LF guardado actualmente  en la matriz final es menor que LS  se actualiza
                        if self.finalMatrix[i][2] < self.finalMatrix[aux-1][3] or self.finalMatrix[i][2] < self.finalMatrix[aux-1][2]:
                            # Se guarda el valor como LF en la matriz final  para este nodo
                            self.finalMatrix[aux-1][3] = self.finalMatrix[i][2]
                        # Se actualiza LS si es menor que la LF menos la duracion en el nodo actual
                        if self.finalMatrix[i][2] - self.adjMatrixForward[aux-1][i] < self.finalMatrix[aux-1][2]:
                            # se guarda el valor como LS en la matriz final  para el nodo actual
                            self.finalMatrix[aux-1][2] = self.finalMatrix[i][2] - \
                                self.adjMatrixForward[aux-1][i]

            # Si todos los nodos han sido visited se termina el ciclo
            if False not in visited:
                stop = True

    def calculateCPM(self):
      # Se hace el forward pass
        self.forwardPass()
      # Se hace el backward pass
        self.backwardPass()

      # Se calculan las holguras
        slacks = []
        for i in range(len(self.activitiesTable)):
            slack = self.finalMatrix[i][2] - self.finalMatrix[i][0]
            slacks.append([slack])

      # Se da formato a la matriz final
        for i in range(len(self.finalMatrix)):
            self.finalMatrix[i].insert(0, self.activitiesTable[i][2])
            self.finalMatrix[i].insert(0, self.activitiesTable[i][1])
            self.finalMatrix[i].insert(0, self.activitiesTable[i][0])

            slacks[i].insert(0, self.activitiesTable[i][0])

        return {'finalTable': self.finalMatrix, "slacks": slacks}

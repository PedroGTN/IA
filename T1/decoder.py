class decoder:
    #Inicializacao de variaveis, tamanho da instancia,
    #tabela de distancias e coordenadas dos pontos
    size = 0
    dists = []
    coords = []
    
    def __init__(self, instancia):
        arq = open(instancia, 'r')
        lines = arq.readlines()
        self.size = int(lines[0])
        aux = [0] * self.size
        for l in lines[1:]:
            split_coord = l.split()
            self.coords.append([float(split_coord[0]), float(split_coord[1])])

        for i in range(self.size):
            for j in range(self.size):
                aux[j] = self.euclid_dist(i, j)
            self.dists.append(aux.copy())

    #calcula a distancia euclidiana entre dois pontos
    def euclid_dist(self, i, j):
        return ((self.coords[i][0] - self.coords[j][0])**2 + (self.coords[i][1] - self.coords[j][1])**2)**0.5

    #pega a distancia entre dois pontos pela array
    def dist(self, i, j):
        return self.dists[i][j]
    
    #retorna um valor para o tour suprido
    def decode(self, tour):
        tour_mod = []

        for i in range(self.size):
            tour_mod.append([tour[i], i])

        sorted_tour = [[tour[0], 0]] 
        sorted_tour += sorted(tour_mod[1:])

        sum = 0

        for i in range(self.size - 1):
            sum += self.dist(sorted_tour[i][1], sorted_tour[i+1][1])

        sum += self.dist(sorted_tour[0][1], sorted_tour[self.size-1][1])

        return sum

        

        
        


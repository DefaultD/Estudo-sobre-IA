class Vertice:
    def __init__(self, rotulo, distancia_objetivo):
        self.adjacentes = []
        self.rotulo = rotulo
        self.visitado = False
        self.distancia_objetivo = distancia_objetivo
        
    def insereAdjacentes(self, adjacente):
        self.adjacentes.append(adjacente)
        
    def imprimeAdjacentes(self):
        for adjacente in self.adjacentes:
            print(adjacente.vertice.rotulo, '-', adjacente.custo)
class Vertice:
    def __init__(self, rotulo, distancia_objetivo):
        self.rotulo = rotulo
        self.visitado = False
        self.adjacentes = []
        self.distancia_objetivo = distancia_objetivo
        
    def adicionar_adjacente(self, adjacente):
        self.adjacentes.append(adjacente)
    
    def mostrar_adjacentes(self):
        for i in self.adjacentes:
            print(i.vertice.rotulo, i.custo)
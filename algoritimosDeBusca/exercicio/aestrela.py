from vetorOrdenado import VetorOrdenado


class AEstrela:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.encontrado = False
        self.caminho = []
        
    def buscar(self, atual):
        self.caminho.append(atual.rotulo)
        atual.visitado = True
        if atual == self.objetivo:
            self.encontrado = True
        else:
            vetor = VetorOrdenado(len(atual.adjacentes))
            for adjacente in atual.adjacentes:
                if not adjacente.vertice.visitado:
                    adjacente.vertice.visitado = True
                    vetor.insere(adjacente)
            if vetor.valores[0] != None:
                self.buscar(vetor.valores[0].vertice)
    
    def imprime_caminho(self):
        print('Caminho encontrado:')
        print(' -> '.join(self.caminho))
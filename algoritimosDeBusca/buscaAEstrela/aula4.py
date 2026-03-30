
from aestrela import AEstrela
from grafo import Grafo
from vetorOrdenado import VetorOrdenado

grafo = Grafo()
vetor = VetorOrdenado(3)
busca_aestrela = AEstrela(grafo.bucharest)
busca_aestrela.buscar(grafo.arad)
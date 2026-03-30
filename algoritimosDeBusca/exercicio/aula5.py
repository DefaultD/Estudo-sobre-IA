# Nesse exercicio vou usar a busca aestrela por que eu quero fazer o algoritimo que mais chegue no caminho mais rapido.
from aestrela import AEstrela
from grafo import Grafo


grafo = Grafo()
aestrela = AEstrela(grafo.curitiba)
aestrela.buscar(grafo.canoinhas)
aestrela.imprime_caminho()
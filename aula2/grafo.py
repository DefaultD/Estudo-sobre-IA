from vertice import Vertice
from adjacente import Adjacente


class Grafo: 
    arad = Vertice('Arad')
    zerind = Vertice('Zerind')
    oradea = Vertice('Oradea')
    sibiu = Vertice('Sibiu')
    timisoara = Vertice('Timisoara')
    lugoj = Vertice('Lugoj')
    mehadia = Vertice('Mehadia')
    dobreta = Vertice('Dobreta')
    craiova = Vertice('Craiova')
    riminicu = Vertice('Riminicu')
    fagaras = Vertice('Fagaras')
    pitesti = Vertice('Pitesti')
    bucharest = Vertice('Bucharest')
    giurgiu = Vertice('Giurgiu')
    
    arad.adicionar_adjacente(Adjacente(zerind, 75))
    arad.adicionar_adjacente(Adjacente(sibiu, 140))
    arad.adicionar_adjacente(Adjacente(timisoara, 118))
    
    zerind.adicionar_adjacente(Adjacente(arad, 75))
    zerind.adicionar_adjacente(Adjacente(oradea, 71))
    
    oradea.adicionar_adjacente(Adjacente(zerind, 71))
    oradea.adicionar_adjacente(Adjacente(sibiu, 151))
    
    sibiu.adicionar_adjacente(Adjacente(arad, 140))
    sibiu.adicionar_adjacente(Adjacente(oradea, 151))
    sibiu.adicionar_adjacente(Adjacente(fagaras, 99))
    sibiu.adicionar_adjacente(Adjacente(riminicu, 80))
    
    timisoara.adicionar_adjacente(Adjacente(arad, 118))
    timisoara.adicionar_adjacente(Adjacente(lugoj, 111))
    
    lugoj.adicionar_adjacente(Adjacente(timisoara, 111))
    lugoj.adicionar_adjacente(Adjacente(mehadia, 70))
    
    mehadia.adicionar_adjacente(Adjacente(lugoj, 70))
    mehadia.adicionar_adjacente(Adjacente(dobreta, 75))
    
    dobreta.adicionar_adjacente(Adjacente(mehadia, 75))
    dobreta.adicionar_adjacente(Adjacente(craiova, 120))
    
    craiova.adicionar_adjacente(Adjacente(dobreta, 120))
    craiova.adicionar_adjacente(Adjacente(riminicu, 146))
    craiova.adicionar_adjacente(Adjacente(pitesti, 138))
    
    riminicu.adicionar_adjacente(Adjacente(sibiu, 80))
    riminicu.adicionar_adjacente(Adjacente(craiova, 146))
    riminicu.adicionar_adjacente(Adjacente(pitesti, 97))
    
    fagaras.adicionar_adjacente(Adjacente(sibiu, 99))
    fagaras.adicionar_adjacente(Adjacente(bucharest, 211))
    
    pitesti.adicionar_adjacente(Adjacente(riminicu, 97))
    pitesti.adicionar_adjacente(Adjacente(craiova, 138))
    pitesti.adicionar_adjacente(Adjacente(bucharest, 101))
    
    bucharest.adicionar_adjacente(Adjacente(fagaras, 211))
    bucharest.adicionar_adjacente(Adjacente(pitesti, 101))
    bucharest.adicionar_adjacente(Adjacente(giurgiu, 90))
    
    giurgiu.adicionar_adjacente(Adjacente(bucharest, 90))
from vertice import Vertice
from adjacente import Adjacente

class Grafo:
    porto_uniao      = Vertice('Porto União', 203)
    paulo_frontin    = Vertice('Paulo Frontin', 172)
    canoinhas        = Vertice('Canoinhas', 141)
    tres_barras      = Vertice('Três Barras', 131)
    sao_mateus       = Vertice('São Mateus do Sul', 123)
    irati            = Vertice('Irati', 139)
    curitiba         = Vertice('Curitiba', 0)
    palmeira         = Vertice('Palmeira', 59)
    mafra            = Vertice('Mafra', 94)
    campo_largo      = Vertice('Campo Largo', 27)
    balsa_nova       = Vertice('Balsa Nova', 41)
    lapa             = Vertice('Lapa', 74)
    tijucas_do_sul   = Vertice('Tijucas do Sul', 56)
    araucaria        = Vertice('Araucária', 23)
    sao_jose_pinhais = Vertice('São José dos Pinhais', 13)
    contenda         = Vertice('Contenda', 39)

    # Porto União
    porto_uniao.insereAdjacentes(Adjacente(paulo_frontin, 46))
    porto_uniao.insereAdjacentes(Adjacente(sao_mateus, 87))
    porto_uniao.insereAdjacentes(Adjacente(canoinhas, 78))

    # Paulo Frontin
    paulo_frontin.insereAdjacentes(Adjacente(porto_uniao, 46))
    paulo_frontin.insereAdjacentes(Adjacente(irati, 75))

    # Irati
    irati.insereAdjacentes(Adjacente(paulo_frontin, 75))
    irati.insereAdjacentes(Adjacente(sao_mateus, 57))
    irati.insereAdjacentes(Adjacente(palmeira, 75))

    # São Mateus do Sul
    sao_mateus.insereAdjacentes(Adjacente(porto_uniao, 87))
    sao_mateus.insereAdjacentes(Adjacente(irati, 57))
    sao_mateus.insereAdjacentes(Adjacente(tres_barras, 43))
    sao_mateus.insereAdjacentes(Adjacente(lapa, 60))
    sao_mateus.insereAdjacentes(Adjacente(palmeira, 77))

    # Palmeira
    palmeira.insereAdjacentes(Adjacente(irati, 75))
    palmeira.insereAdjacentes(Adjacente(campo_largo, 55))
    palmeira.insereAdjacentes(Adjacente(sao_mateus, 77))

    # Canoinhas
    canoinhas.insereAdjacentes(Adjacente(porto_uniao, 78))
    canoinhas.insereAdjacentes(Adjacente(tres_barras, 12))
    canoinhas.insereAdjacentes(Adjacente(mafra, 66))

    # Três Barras
    tres_barras.insereAdjacentes(Adjacente(sao_mateus, 43))
    tres_barras.insereAdjacentes(Adjacente(canoinhas, 12))

    # Mafra
    mafra.insereAdjacentes(Adjacente(canoinhas, 66))
    mafra.insereAdjacentes(Adjacente(lapa, 57))
    mafra.insereAdjacentes(Adjacente(tijucas_do_sul, 99))

    # Campo Largo
    campo_largo.insereAdjacentes(Adjacente(palmeira, 55))
    campo_largo.insereAdjacentes(Adjacente(balsa_nova, 22))
    campo_largo.insereAdjacentes(Adjacente(curitiba, 29))

    # Balsa Nova
    balsa_nova.insereAdjacentes(Adjacente(campo_largo, 22))
    balsa_nova.insereAdjacentes(Adjacente(contenda, 19))
    balsa_nova.insereAdjacentes(Adjacente(curitiba, 51))

    # Lapa
    lapa.insereAdjacentes(Adjacente(sao_mateus, 60))
    lapa.insereAdjacentes(Adjacente(mafra, 57))
    lapa.insereAdjacentes(Adjacente(contenda, 26))

    # Contenda
    contenda.insereAdjacentes(Adjacente(balsa_nova, 19))
    contenda.insereAdjacentes(Adjacente(lapa, 26))
    contenda.insereAdjacentes(Adjacente(araucaria, 18))

    # Araucária
    araucaria.insereAdjacentes(Adjacente(contenda, 18))
    araucaria.insereAdjacentes(Adjacente(curitiba, 37))

    # Curitiba
    curitiba.insereAdjacentes(Adjacente(campo_largo, 29))
    curitiba.insereAdjacentes(Adjacente(balsa_nova, 51))
    curitiba.insereAdjacentes(Adjacente(araucaria, 37))
    curitiba.insereAdjacentes(Adjacente(sao_jose_pinhais, 15))

    # Tijucas do Sul
    tijucas_do_sul.insereAdjacentes(Adjacente(mafra, 99))
    tijucas_do_sul.insereAdjacentes(Adjacente(sao_jose_pinhais, 49))

    # São José dos Pinhais
    sao_jose_pinhais.insereAdjacentes(Adjacente(curitiba, 15))
    sao_jose_pinhais.insereAdjacentes(Adjacente(tijucas_do_sul, 49))

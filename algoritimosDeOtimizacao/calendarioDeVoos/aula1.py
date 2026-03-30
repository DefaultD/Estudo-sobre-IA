from pprint import pprint
pessoas = [
    ('Lisboa', 'LIS'),
    ('Madrid', 'MAD'),
    ('Paris', 'CDG'),
    ('Dublin', 'DUB'),
    ('Bruxelas', 'BRU'),
    ('Londres', 'LHR'),
]

destno = 'FCO'

voos = {}

for linha in open(r'C:\Users\KaueSobral\Documents\Projetos\curso_python\algoritimosDeOtimizacao\calendarioDeVoos\flights.txt'):
    origem, destino, saida, chegada, preco = linha.split(',')
    voos.setdefault((origem, destino), [])
    voos[(origem, destino)].append((saida, chegada, int(preco)))
    
    
pprint(voos[('FCO','LIS')])
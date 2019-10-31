from random import randint
from time import sleep
jogadores = {}
for n in range(1, 5):
        jogadores['jogador ' + str(n)] = randint(1, 12)
        sleep(1)
        print(f'Jogador {n} jogou o dado e obteve o valor: {jogadores["jogador " + str(n)]}')
print(f'Vamos para os resultados...\n\n{"Resultados":~^40}\n')
z = 0
for c, n in enumerate(sorted(jogadores.values(), reverse=True)):
        for r in jogadores.keys():
                if z == n:
                        break
                if jogadores[r] == n:
                        print(f'O {r} ficou em {c + 1}º lugar')
                        sleep(0.5)
        z = n

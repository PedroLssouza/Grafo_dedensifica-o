import random
import matplotlib.pyplot as plt

# Inicialização
nos = set()
arestas = set()
historico_n = []
historico_m = []

# Parâmetros
passos = 10
novos_nos_por_passo = 10
arestas_por_passo = 5

proximo_id = 0

for passo in range(passos):
    # Adiciona novos nós
    novos_nos = list(range(proximo_id, proximo_id + novos_nos_por_passo))
    nos.update(novos_nos)
    proximo_id += novos_nos_por_passo

    # Adiciona arestas aleatórias entre os novos nós e os existentes
    todos_nos = list(nos)
    for _ in range(arestas_por_passo):
        if len(todos_nos) < 2:
            continue
        u = random.choice(novos_nos)
        v = random.choice(todos_nos)
        if u != v:
            aresta = tuple(sorted((u, v)))
            arestas.add(aresta)

    # Armazena estatísticas
    n = len(nos)
    m = len(arestas)
    densidade = (2 * m) / (n * (n - 1)) if n > 1 else 0
    historico_n.append(n)
    historico_m.append(m)

# Calcula densidade ao longo do tempo
densidade_total = [ (2*m)/(n*(n-1)) if n > 1 else 0 for n, m in zip(historico_n, historico_m)]

# Plot
plt.figure(figsize=(10, 5))
plt.plot(historico_n, densidade_total, marker='o')
plt.title("Densidade do grafo ao longo do tempo (dedensificação)")
plt.xlabel("Número de nós")
plt.ylabel("Densidade do grafo")
plt.grid(True)
plt.show()
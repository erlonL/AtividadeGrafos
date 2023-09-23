## Teste 2 DFS - PCV10

from graph import Graph
from main import load_from

gr = load_from("../instncias_grafo/pcv10.txt")

# gr.print_adjs()

# print(gr.bfs(0))

print("DFS com recursividade\nlista de vértices pai: {}".format(gr.dfs()))
print()
print("DFS com pilha\nlista de vértices pai: {}".format(gr.dfs_pilha()))


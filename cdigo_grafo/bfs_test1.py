## TESTE 1 - PCV4

from main import load_from
from graph import Graph

gr = load_from("../instncias_grafo/pcv4.txt")

gr.print_adjs()
print()

v1 = 0
v2 = 3
print("v1: {}, v2: {}".format(v1, v2))
path = gr.bfs_search(v1, v2); print("Caminho: {}".format(path))
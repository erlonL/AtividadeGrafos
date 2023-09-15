## TESTE 3 - PCV50

from main import load_from
from graph import Graph

gr = load_from("../instncias_grafo/pcv50.txt")

# gr.print_adjs()

v1 = 15
v2 = 8
print("v1: {}, v2: {}".format(v1, v2))
path = gr.bfs_search(v1, v2); print("Caminho: {}".format(path))
## TESTE 2 - PCV10

from main import load_from
from graph import Graph

gr = load_from("../instncias_grafo/pcv10.txt")

gr.print_adjs()

v1 = 8
v2 = 2
print("v1: {}, v2: {}".format(v1, v2))
path = gr.bfs_search(v1, v2); print("Caminho: {}".format(path))
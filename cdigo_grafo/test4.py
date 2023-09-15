## TESTE 4 - PCV177

from main import load_from
from graph import Graph
import random

gr = load_from("../instncias_grafo/pcv177.txt")

# gr.print_adjs()

v1 = random.randint(0, gr.num_vertices - 1)
v2 = random.randint(0, gr.num_vertices - 1)
print("v1: {}, v2: {}".format(v1, v2))
path = gr.bfs_search(v1, v2); print("Caminho: {}".format(path))
## Implementação da estrutura de <b>Grafos</b> em Python.

- [x] Leitura de arquivos e carregamento das estruturas do Grafo
- [x] Busca em largura (BFS)
    - [x] Método bfs_search(v1, v2) para imprimir o caminho entre dois vértices. Se não houver, indica que não há caminho.

- [ ] Busca em Profundidade (DFS)
    - [ ] Reimplementação do DFS com auxílio de uma pilha para eliminar a recursão da implementação.


### Veja: [Testes](#veja-testes)


[<h2>Testes</h2>](#veja-testes)
<img src="media/test1_2.png" alt="test1_test2">

### Execução Testes
```bash
>> python3 test1.py
Listas de adjacências
0 - [1, 2]
1 - [0, 2, 3]
2 - [0, 1]
3 - [1]

v1: 0, v2: 3
Caminho: [0, 1, 3]
```

```bash
>> python3 test2.py
Listas de adjacências
0 - [1]
1 - [0]
2 - [3, 4, 5, 6]
3 - [2, 4, 5, 6]
4 - [2, 3, 5, 6, 7]
5 - [2, 3, 4, 6, 7]
6 - [2, 3, 4, 5, 7]
7 - [4, 5, 8, 9]
8 - [7, 9]
9 - [7, 8]
v1: 8, v2: 2
Caminho: [8, 7, 4, 2]
```

```bash
>> python3 test3.py
[...]
```

```bash
>> python3 test4.py
[...]
```
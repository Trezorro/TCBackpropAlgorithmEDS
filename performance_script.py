# %%
import numpy as np
import networkx as nx

# %%
def init():
    global C, N, S, G, count
    count = 0
    C = np.zeros((10,10), dtype='int')
    # N = np.random.randint(2, size=(10,10), )
    N = np.array([
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]])
    S = N.copy()
    G = nx.DiGraph(S)

def init2(size = 10):
    global C, N, S, G, count
    count = 0
    C = np.zeros((size,size), dtype='int')
    N = np.random.randint(2, size=(size,size), ) & np.random.randint(2, size=(size,size), )
    S = N.copy()
    G = nx.DiGraph(S)

def init15example():
    global C, N, S, G, count
    count = 0
    C = np.zeros((15,15), dtype='int')
    N = np.array([[0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1],
       [0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1],
       [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1],
       [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
       [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
       [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
       [0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1],
       [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0]])
    S = N.copy()
    G = nx.DiGraph(S)

def reset_N_and_C():
    global C, N, S, G, count
    count = 0
    C[:] = 0
    N = S.copy()
    S = N.copy()
    G = nx.DiGraph(S)

def initempty(size = 10):
    global C, N, S, G, count
    count = 0
    C = np.zeros((size,size), dtype='int')
    N = np.zeros((size,size), dtype='int')
    S = N.copy()
    G = nx.DiGraph(S)


def init_from_nx(graph):
    global C, N, S, G, count
    count = 0
    N = nx.to_numpy_array(graph, dtype='int')
    C = np.zeros_like(N)
    S = N.copy()
    G = nx.DiGraph(S)
    # G = graph

init()

# %%
def explore(s, root):
    for t in N[s].nonzero()[0]:
        if not C[root,t]: # needs to be checked as many times as N has ones.
            C[root, t] = 1 # after exploring, this node known by the root.
            N[s,t] = 0 # pop this front (covered in N update below)
            explore(t, root)
            C[s] |= C[t] # pull target's cover into current node
            C[s,t] = 1 # and add the target itself to the cover
            N[s] = ~C[s] & (N[s] | N[t])

# %% [markdown]
# # Test Complete Solve Time

def solve_kleene():
    global G
    for root in range(G.number_of_nodes()):
        explore(root, root)

V = 2000
# graph = nx.random_k_out_graph(V, 3, 3)
# graph = nx.binomial_tree(5)
graph = nx.soft_random_geometric_graph(V, .1)
init_from_nx(graph)


# %%
print(N.sum())

# %%

solve_kleene()
print(N.sum())
print(C.sum())

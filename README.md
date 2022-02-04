# Transitive Closure Algorithm Visualized
For the 2IMD10 (2021-GS2) Engineering Data Systems course.

https://user-images.githubusercontent.com/19216539/152614331-7f51ae26-f500-40ba-a13f-a78ed9a9f676.mp4

_The transitive closure is first solved from the perspective of node 0. A later query on node 1 uses the cached results._

## Environment Setup
With Conda (miniconda) installed, in your shell, run:
`conda env create -f graph_env.yml`

## Usage
testgraph.ipynb is the file of interest. I recommend opening it in vscode as it's support for notebooks has gotten quite awesome.

It uses global variables for everything, so run an `init()` function first to initialize `C` and `N`, then run the Tresoor Closure Algorithm by calling 
`explore(root_idx, root_idx)`

To see it's steps, visualized using matplotlib in a separate window, uncomment the `# drawnext(...)` calls in the algo definition:
```
def explore(s, root):
    # drawnext(s, explore=True)
    for t in N[s].nonzero()[0]:
        if not C[root,t]: # needs to be checked as many times as N has ones.
            C[root, t] = 1 # after exploring, this node known by the root.
            N[s,t] = 0 # pop this front (covered in N update below)
            explore(t, root)
            C[s] |= C[t] # pull target's cover into current node
            C[s,t] = 1 # and add the target itself to the cover
            N[s] = ~C[s] & (N[s] | N[t])
```
## Larger example


https://user-images.githubusercontent.com/19216539/152614318-811568da-9d9f-4e0f-83a4-2a23cfced47a.mp4




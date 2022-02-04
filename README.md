# Transitive Closure Algorithm Visualized
For the 2IMD10 (2021-GS2) Engineering Data Systems course.

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



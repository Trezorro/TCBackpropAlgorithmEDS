# Transitive Closure Algorithm Visualized
For the 2IMD10 (2021-GS2) Engineering Data Systems course.

https://user-images.githubusercontent.com/19216539/152614331-7f51ae26-f500-40ba-a13f-a78ed9a9f676.mp4

_The transitive closure is first solved from the perspective of root node 0. A later query on node 1 uses the cached backpropagation results. Generated using the notebook in this repo._


## Algorithm
Given the matrices C, N, E:
- **C** (VxV) (partial closure, visualized in **black**), and
- **N** (VxV) (wavefront, visualized in **red**), on
- graph G(V,E) (basegraph, with E vizualized in blue),

the recursive algorithm for solving the transitive closure for `root` is defined as follows:
```
def explore(s: int, root: int):
    for t in N[s].nonzero()[0]:    # loop over current wavefront (targets yet to be explored)
        if not C[root,t]:          # Only explore deeper if root node does not yet have t in it's closure.
            C[root, t] = 1         # Register t as known to root node.
            if t == root:          # if root reaches back to itself, prevent cyclic recursion.
                N[root,t] = 0      # Maintain first invariant for this special case.
                continue
            explore(t, root)       # recurse on target t
                                   # Backpropagation:
            C[s] |= C[t]                 # Pull target's partial cover into current node s
            C[s,t] = 1                   # And add the target itself to the cover
            N[s] = ~C[s] & (N[s] | N[t]) # Maintain invariant (Ns' = (Ns U Nt) \ Cs )
```

When a call `explore(r, r)` returns, the root node r will be fully explored, and it transitive closure can be obtained from C[r].

### Invariants
At the start and end of each recursive call, the following invariants hold for source node s:
 * **C**[s] and **N**[s] are disjoint, and:
 * For any transitively reachable target t ∈ **TC**(s), of source node s, we have:
   - t is either already in (partial) closure **C**[s],
   - t ∈ **N**[s]
   - t ∈ TC(t') for some t' ∈ **N**[s]

A node s is fully explored when partial closure **C**(s)=**TC**(s)
Then, the invariants give us that a node s is fully explored _iff_  **N**(s) = **{}**

When the call `explore(r, r)` (depth 0) returns, the root node r will be fully explored.

### Larger example
Note:
Nodes are highlighted in **red** when explore starts a recursing on them, **green** when returning to their caller, and **blue** when they have just taken backpropagated results from the last explored target. Nodes will be red and green at most once per recursive search, i.e. only visited once, and only when necessary for the root node.

During backpropagation, the partial closure of a node s is updated with the partial closure of an explored target t. You can see how this shared knowlegde propagates throughout the graph looking at the black edges. Red edges denote what targets a node still would need to check and explore to guarantuee completion of it's own transitive closure.

https://user-images.githubusercontent.com/19216539/152614318-811568da-9d9f-4e0f-83a4-2a23cfced47a.mp4


# Usage
## Environment Setup
With Conda (miniconda) installed, in your shell, run:
`conda env create -f graph_env.yml`

## Notebook Usage
**testgraph.ipynb** is the main file of interest. I recommend opening it in vscode as it's support for notebooks has gotten quite awesome.

It uses global variables for everything, so run an `init()` function first to initialize `C` and `N`, then run the Transitive Closure Algorithm by calling 
`explore(root_idx, root_idx)`

To see it's steps, visualized using matplotlib in a separate window, use the `#explore_debug()` definitiion instead of the `explore()` function definition. 





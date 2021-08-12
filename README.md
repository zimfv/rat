# RAT - Restoring Aggregated Tables
## What's the problem?

There are two aggregated tables with some concided columns:

| Name | A_1 |  <img src="https://latex.codecogs.com/gif.latex?A_2"/> | ... | $A_n$ |
| --- | --- | --- | --- | --- |
| $\text{Name}_1$ | $a_1^1$ | $a_2^1$ | ... | $a_n^1$ |
| $\text{Name}_2$ | $a_1^2$ | $a_2^2$ | ... | $a_n^2$ |
| ... | ... | ... | ... | ... |
| $\text{Name}_N$ | $a_1^N$ | $a_2^N$ | ... | $a_n^N$ |

| Name | $B_1$ |  $B_2$ | ... | $B_m$ |
| --- | --- | --- | --- | --- |
| $\text{Name}_1$ | $b_1^1$ | $b_2^1$ | ... | $b_m^1$ |
| $\text{Name}_2$ | $b_1^2$ | $b_2^2$ | ... | $b_m^2$ |
| ... | ... | ... | ... | ... |
| $\text{Name}_N$ | $b_1^N$ | $b_2^N$ | ... | $b_m^N$ |

Where

<img src="https://latex.codecogs.com/gif.latex?
\sum\limits_{i=1}^n a_i^k =
\sum\limits_{j=1}^m b_j^k = S^k
"/>

I want to "restore" (disaggregate) them somehow to get new table

| Name | A | B | X |
| --- | --- | --- | --- |
| $\text{Name}_1$ | $A_1$ | $B_1$ | $x_{1, 1}^1$ |
| $\text{Name}_1$ | $A_1$ | $B_2$ | $x_{1, 2}^1$ |
| ... | ... | ... | ... |
| $\text{Name}_1$ | $A_n$ | $B_m$ | $x_{n, m}^1$ |
| $\text{Name}_2$ | $A_1$ | $B_1$ | $x_{1, 1}^2$ |
| ... | ... | ... | ... |
| $\text{Name}_N$ | $A_n$ | $B_m$ | $x_{n, m}^N$ |

Such that

<img src="https://latex.codecogs.com/gif.latex?
\begin{cases}
a^k_i = \sum\limits_{j=1}^m x^k_{ij}
b^k_i = \sum\limits_{i=1}^n x^k_{ij}
\end{cases}
\forall i \in \{1, ..., n\}, j \in \{1, ..., m\}, k \in \{1, ..., N\}
"/>


## Solving the problem

Of course there exists a lot of solves for that's system. So I make a guess that results are most independent. 
$$
\cfrac{a_i^k}{S^k} \cfrac{b_j^k}{S^k} - \cfrac{x_{ij}^k}{S^k} \to 0
$$
Independence is not possible in general situation, so i will minimize N sums
$$
\sum\limits_{i=1}^n \sum\limits_{j=1}^m \left[\cfrac{a_i^k}{S^k} \cfrac{b_j^k}{S^k} - \cfrac{x_{ij}^k}{S^k}\right]^2
$$
by minimizing equivalent
$$
\sum\limits_{i=1}^n\sum\limits_{j=1}^m \left({x^k_{ij}}\right)^2
$$

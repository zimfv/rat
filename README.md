# RAT - Restoring Aggregated Tables
## What's the problem?

There are two aggregated tables with some concided columns:

| Name | A_1 | A_2 | ... | A_n |
| --- | --- | --- | --- | --- |
| Name_1 | $a_1^1$ <img src="https://latex.codecogs.com/gif.image?\dpi{110}&space;\bg_white&space;a_1^1" title="\bg_white a_1^1" /> | $a_2^1$ | ... | $a_n^1$ |
| Name_2 | $a_1^2$ | $a_2^2$ | ... | $a_n^2$ |
| ... | ... | ... | ... | ... |
| Name_N | $a_1^N$ | $a_2^N$ | ... | $a_n^N$ |

| Name | B_1 | B_2 | ... | B_m |
| --- | --- | --- | --- | --- |
| Name_1 | $b_1^1$ | $b_2^1$ | ... | $b_m^1$ |
| Name_2 | $b_1^2$ | $b_2^2$ | ... | $b_m^2$ |
| ... | ... | ... | ... | ... |
| Name_N | $b_1^N$ | $b_2^N$ | ... | $b_m^N$ |

Where

<!-- $ \sum\limits_{i=1}^n a_i^k = \sum\limits_{j=1}^m b_j^k = S^k $ -->

<img src="https://latex.codecogs.com/gif.image?\dpi{110}&space;\bg_white&space;\sum\limits_{i=1}^n&space;a_i^k&space;=&space;\sum\limits_{j=1}^m&space;b_j^k&space;=&space;S^k" title="\bg_white \sum\limits_{i=1}^n a_i^k = \sum\limits_{j=1}^m b_j^k = S^k" />

I want to "restore" (disaggregate) them somehow to get new table

| Name | A | B | X |
| --- | --- | --- | --- |
| Name_1 | A_1 | B_1 | $x_{1, 1}^1$ |
| Name_1 | A_1 | B_2 | $x_{1, 2}^1$ |
| ... | ... | ... | ... |
| Name_1 | A_n | B_m | $x_{n, m}^1$ |
| Name_2 | A_1 | B_1 | $x_{1, 1}^2$ |
| ... | ... | ... | ... |
| Name_N | A_n | B_m | $x_{n, m}^N$ |

Such that

<!-- $ \begin{cases} a^k_i = \sum\limits_{j=1}^m x^k_{ij} \\ b^k_i = \sum\limits_{i=1}^n x^k_{ij} \end{cases} \forall i \in {1, ..., n}, j \in {1, ..., m}, k \in {1, ..., N} $ -->
<img src="https://latex.codecogs.com/gif.image?\dpi{110}&space;\bg_white&space;\begin{cases}&space;a^k_i&space;=&space;\sum\limits_{j=1}^m&space;x^k_{ij}&space;\\&space;b^k_i&space;=&space;\sum\limits_{i=1}^n&space;x^k_{ij}&space;\end{cases}&space;\forall&space;i&space;\in&space;{1,&space;...,&space;n},&space;j&space;\in&space;{1,&space;...,&space;m},&space;k&space;\in&space;{1,&space;...,&space;N}" title="\bg_white \begin{cases} a^k_i = \sum\limits_{j=1}^m x^k_{ij} \\ b^k_i = \sum\limits_{i=1}^n x^k_{ij} \end{cases} \forall i \in {1, ..., n}, j \in {1, ..., m}, k \in {1, ..., N}" />

## Solving the problem

Of course there exists a lot of solves for that's system. So I make a guess that results are most independent. 

<!-- $ \cfrac{a_i^k}{S^k} \cfrac{b_j^k}{S^k} - \cfrac{x_{ij}^k}{S^k} \to 0 $ -->
<img src="https://latex.codecogs.com/gif.image?\dpi{110}&space;\bg_white&space;&space;\cfrac{a_i^k}{S^k}&space;\cfrac{b_j^k}{S^k}&space;-&space;\cfrac{x_{ij}^k}{S^k}&space;\to&space;0" title="\bg_white  \cfrac{a_i^k}{S^k} \cfrac{b_j^k}{S^k} - \cfrac{x_{ij}^k}{S^k} \to 0" />

Independence is not possible in general situation, so i will minimize N sums

<!-- $ \sum\limits_{i=1}^n \sum\limits_{j=1}^m \left[\cfrac{a_i^k}{S^k} \cfrac{b_j^k}{S^k} - \cfrac{x_{ij}^k}{S^k}\right]^2 $ -->
<img src="https://latex.codecogs.com/gif.image?\dpi{110}&space;\bg_white&space;\sum\limits_{i=1}^n&space;\sum\limits_{j=1}^m&space;\left[\cfrac{a_i^k}{S^k}&space;\cfrac{b_j^k}{S^k}&space;-&space;\cfrac{x_{ij}^k}{S^k}\right]^2" title="\bg_white \sum\limits_{i=1}^n \sum\limits_{j=1}^m \left[\cfrac{a_i^k}{S^k} \cfrac{b_j^k}{S^k} - \cfrac{x_{ij}^k}{S^k}\right]^2" />

by minimizing equivalent

<!-- $ \sum\limits_{i=1}^n\sum\limits_{j=1}^m \left({x^k_{ij}}\right)^2 $ -->
<img src="https://latex.codecogs.com/gif.image?\dpi{110}&space;\bg_white&space;\sum\limits_{i=1}^n\sum\limits_{j=1}^m&space;\left({x^k_{ij}}\right)^2" title="\bg_white \sum\limits_{i=1}^n\sum\limits_{j=1}^m \left({x^k_{ij}}\right)^2" />

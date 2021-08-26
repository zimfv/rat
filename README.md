# RAT - Restoring Aggregated Tables
## What's the problem?

There are two aggregated tables with some concided columns:

<!--
| Name | A_1 | A_2 | ... | A_n |
| --- | --- | --- | --- | --- |
| Name_1 | $a_1^1$ | $a_2^1$ | ... | $a_n^1$ |
| Name_2 | $a_1^2$ | $a_2^2$ | ... | $a_n^2$ |
| ... | ... | ... | ... | ... |
| Name_N | $a_1^N$ | $a_2^N$ | ... | $a_n^N$ |
-->
<img src="https://latex.codecogs.com/gif.image?\dpi{110}&space;\bg_white&space;&space;\begin{tabular}{|c|c|c|c|c|}\hline\textbf{Name}&space;&&space;$\textbf{A}_1$&space;&&space;$\textbf{A}_2$&space;&&space;$\cdots$&space;&&space;$\textbf{A}_n$&space;\\\hline$Name_1$&space;&&space;$a_1^1$&space;&&space;$a_2^1$&space;&&space;$\cdots$&space;&&space;$a_n^1$&space;\\\hline$Name_2$&space;&&space;$a_1^2$&space;&&space;$a_2^2$&space;&&space;$\cdots$&space;&&space;$a_n^2$&space;\\\hline$\cdots$&space;&&space;$\cdots$&space;&&space;$\cdots$&space;&&space;$\cdots$&space;&&space;$\cdots$&space;\\\hline$Name_N$&space;&&space;$a_1^N$&space;&&space;$a_2^N$&space;&&space;$\cdots$&space;&&space;$a_n^N$&space;\\\hline\end{tabular}" title="\bg_white \begin{tabular}{|c|c|c|c|c|}\hline\textbf{Name} & $\textbf{A}_1$ & $\textbf{A}_2$ & $\cdots$ & $\textbf{A}_n$ \\\hline$Name_1$ & $a_1^1$ & $a_2^1$ & $\cdots$ & $a_n^1$ \\\hline$Name_2$ & $a_1^2$ & $a_2^2$ & $\cdots$ & $a_n^2$ \\\hline$\cdots$ & $\cdots$ & $\cdots$ & $\cdots$ & $\cdots$ \\\hline$Name_N$ & $a_1^N$ & $a_2^N$ & $\cdots$ & $a_n^N$ \\\hline\end{tabular}" />

<!--
| Name | B_1 | B_2 | ... | B_m |
| --- | --- | --- | --- | --- |
| Name_1 | $b_1^1$ | $b_2^1$ | ... | $b_m^1$ |
| Name_2 | $b_1^2$ | $b_2^2$ | ... | $b_m^2$ |
| ... | ... | ... | ... | ... |
| Name_N | $b_1^N$ | $b_2^N$ | ... | $b_m^N$ |
-->
<img src="https://latex.codecogs.com/gif.image?\dpi{110}&space;\bg_white&space;\inline&space;\begin{tabular}{|c|c|c|c|c|}\hline\textbf{Name}&space;&&space;$\textbf{B}_1$&space;&&space;$\textbf{B}_2$&space;&&space;$\cdots$&space;&&space;$\textbf{B}_m$&space;\\\hline$Name_1$&space;&&space;$b_1^1$&space;&&space;$b_2^1$&space;&&space;$\cdots$&space;&&space;$b_m^1$&space;\\\hline$Name_2$&space;&&space;$b_1^2$&space;&&space;$b_2^2$&space;&&space;$\cdots$&space;&&space;$b_m^2$&space;\\\hline$\cdots$&space;&&space;$\cdots$&space;&&space;$\cdots$&space;&&space;$\cdots$&space;&&space;$\cdots$&space;\\\hline$Name_N$&space;&&space;$b_1^N$&space;&&space;$b_2^N$&space;&&space;$\cdots$&space;&&space;$b_m^N$&space;\\\hline\end{tabular}" title="\bg_white \inline \begin{tabular}{|c|c|c|c|c|}\hline\textbf{Name} & $\textbf{B}_1$ & $\textbf{B}_2$ & $\cdots$ & $\textbf{B}_m$ \\\hline$Name_1$ & $b_1^1$ & $b_2^1$ & $\cdots$ & $b_m^1$ \\\hline$Name_2$ & $b_1^2$ & $b_2^2$ & $\cdots$ & $b_m^2$ \\\hline$\cdots$ & $\cdots$ & $\cdots$ & $\cdots$ & $\cdots$ \\\hline$Name_N$ & $b_1^N$ & $b_2^N$ & $\cdots$ & $b_m^N$ \\\hline\end{tabular}" />

Where

<!-- $ \sum\limits_{i=1}^n a_i^k = \sum\limits_{j=1}^m b_j^k = S^k $ -->
<img src="https://latex.codecogs.com/gif.image?\dpi{110}&space;\bg_white&space;\sum\limits_{i=1}^n&space;a_i^k&space;=&space;\sum\limits_{j=1}^m&space;b_j^k&space;=&space;S^k" title="\bg_white \sum\limits_{i=1}^n a_i^k = \sum\limits_{j=1}^m b_j^k = S^k" />

I want to "restore" (disaggregate) them somehow to get new table

<!--
| Name | A | B | X |
| --- | --- | --- | --- |
| Name_1 | A_1 | B_1 | $x_{1, 1}^1$ |
| Name_1 | A_1 | B_2 | $x_{1, 2}^1$ |
| ... | ... | ... | ... |
| Name_1 | A_n | B_m | $x_{n, m}^1$ |
| Name_2 | A_1 | B_1 | $x_{1, 1}^2$ |
| ... | ... | ... | ... |
| Name_N | A_n | B_m | $x_{n, m}^N$ |
-->
<img src="https://latex.codecogs.com/gif.image?\dpi{110}&space;\bg_white&space;\inline&space;\begin{tabular}{|c|c|c|c|}\hline\textbf{Name}&space;&&space;\textbf{A}&space;&&space;\textbf{B}&space;&&space;\textbf{X}&space;\\\hline$Name_1$&space;&&space;$A_1$&space;&&space;$B_1$&space;&&space;$x_{1,&space;1}^1$&space;\\\hline$Name_1$&space;&&space;$A_1$&space;&&space;$B_2$&space;&&space;$x_{1,&space;2}^1$&space;\\\hline$\cdots$&space;&&space;$\cdots$&space;&&space;$\cdots$&space;&&space;$\cdots$&space;\\\hline$Name_1$&space;&&space;$A_n$&space;&&space;$B_m$&space;&&space;$x_{n,&space;m}^1$&space;\\\hline$Name_2$&space;&&space;$A_1$&space;&&space;$B_1$&space;&&space;$x_{1,&space;1}^2$&space;\\\hline$\cdots$&space;&&space;$\cdots$&space;&&space;$\cdots$&space;&&space;$\cdots$&space;\\\hline$Name_N$&space;&&space;$A_n$&space;&&space;$B_m$&space;&&space;$x_{n,&space;m}^N$&space;\\\hline\end{tabular}" title="\bg_white \inline \begin{tabular}{|c|c|c|c|}\hline\textbf{Name} & \textbf{A} & \textbf{B} & \textbf{X} \\\hline$Name_1$ & $A_1$ & $B_1$ & $x_{1, 1}^1$ \\\hline$Name_1$ & $A_1$ & $B_2$ & $x_{1, 2}^1$ \\\hline$\cdots$ & $\cdots$ & $\cdots$ & $\cdots$ \\\hline$Name_1$ & $A_n$ & $B_m$ & $x_{n, m}^1$ \\\hline$Name_2$ & $A_1$ & $B_1$ & $x_{1, 1}^2$ \\\hline$\cdots$ & $\cdots$ & $\cdots$ & $\cdots$ \\\hline$Name_N$ & $A_n$ & $B_m$ & $x_{n, m}^N$ \\\hline\end{tabular}" />

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

Or we can just minimize

<!-- $ \sum\limits_{i=1}^n\sum\limits_{j=1}^m \left({x^k_{ij}}\right)^2 $ -->
<img src="https://latex.codecogs.com/gif.image?\dpi{110}&space;\bg_white&space;\sum\limits_{i=1}^n\sum\limits_{j=1}^m&space;\left({x^k_{ij}}\right)^2" title="\bg_white \sum\limits_{i=1}^n\sum\limits_{j=1}^m \left({x^k_{ij}}\right)^2" />


## Usage examples
### Restoring two tables

```python
import numpy as np
import pandas as pd
```

There are two tables: __employment__ with columns __District__, __Agriculture__, __Industry__, __Production__, __Service__; 


```python
df_employment = pd.read_csv('tables/employment.csv')
df_employment
```
|	 | District | Agriculture | Industry | Production | Service |
| --- | --- | --- |  --- |  --- |  --- | 
| 0 | East Forests | 2063 | 3644 | 504 | 5562 |
| 1 | North Mountains | 1258 | 3807 | 862 | 11540 |

and __environment__ with columns __District__, __Urban__, __Suburban__, __Rural__. 

```python
df_environment = pd.read_csv('tables/environment.csv')
df_environment
```
| | District | Urban | Suburban | Rural |
| --- |  --- |  --- |  --- |  --- |
| 0 | East Forests | 3866 | 1510 | 6397 |
| 1 | North Mountains | 3438 | 5779 | 8250 |

So there is column __District__ in both tables.

We want to "restore" that by making them more independence. That we can make with function `restore_table` from `ratrestore` module

```python
from rat.ratrestore import restore_table
df_restored = restore_table(df_employment, df_environment, name_a='Employment', name_b='Environment', name_res='Count')
df_restored.head(6)
```
| |	District |	Employment |	Environment |	Count |
| --- | --- | --- | --- | --- |
| 0 |	East Forests |	Agriculture |	Rural |	1120.955661 |	
| 1 |	East Forests |	Agriculture |	Suburban |	264.599508 |	
| 2 |	East Forests |	Agriculture |	Urban |	677.444831 |	
| 3 |	East Forests |	Industry |	Rural |	1980.010872 |	
| 4 |	East Forests |	Industry |	Suburban |	467.377899 |	
| 5 |	East Forests |	Industry |	Urban |	1196.611229 |	


If we want to "restore" that by making minimal square sums, we can change parameter `obj_type` from default `'dependences'` to `'squares'`:

```python
df_restored = restore_table(df_employment, df_environment, name_a='Employment', name_b='Environment', name_res='Count', obj_type='squares')
df_restored.head(6)
```
| |	District |	Employment |	Environment |	Count |
| --- | --- | --- | --- | --- |
| 0 |	East Forests |	Agriculture |	Rural |	1268.107791 |	
| 1 |	East Forests |	Agriculture |	Suburban |	244.740815 |	
| 2 |	East Forests |	Agriculture |	Urban |	611.218573 |	
| 3 |	East Forests |	Industry |	Rural |	2161.590402 |	
| 4 |	East Forests |	Industry |	Suburban |	129.786239 |	
| 5 |	East Forests |	Industry |	Urban |	1504.701185 |	


### Editing

Suppose we have DataFrame `df_family`

```python
df_family = pd.read_csv('tables/family.csv')
df_family
```
|  | District | Sex | Single | Marriged | Widower |
| --- | --- | --- | --- | --- | --- |
| 0 |	East Forests | Female | 2545 | 2248 | 314 |
| 1 | East Forests | Male | 1702 | 2920 | 2044 |
| 2 | North Mountains | Female | 3059 | 3352 | 617 |
| 3 | North Mountains | Male | 3207 | 4578 | 2654 |

But we want to make one column __Family Status__ from columns __Single__, __Marriged__ and __Widower__.

We can use function `roll_weak` from package `ratedit`

```python
from rat.ratedit ipmort roll_weak
df_family_weak = roll_weak(df_family, ['Single', 'Marriged', 'Widower'], value_name='Family Status', res_name='Persons')
df_family_weak
```
|  | District | Sex | Family Status | Persons |
| --- | --- | --- | --- | --- | 
| 0 | East Forests | Female | Single | 2545 | 
| 1 | East Forests | Female | Marriged | 2248 | 
| 2 | East Forests | Female | Widower | 314 | 
| 3 | East Forests | Male | Single | 1702 | 
| 4 | East Forests | Male | Marriged | 2920 | 
| 5 | East Forests | Male | Widower | 2044 | 
| 6 | North Mountains | Female | Single | 3059 | 
| 7 | North Mountains | Female | Marriged | 3352 | 
| 8 | North Mountains | Female | Widower | 617 | 
| 9 | North Mountains | Male | Single | 3207 | 
| 10 | North Mountains | Male | Marriged | 4578 | 
| 11 | North Mountains | Male | Widower | 2654 | 


Another situation: we want to get df)family with unique values in column __District__ by making columns from values of column __Sex__.

We can use function `roll_strong` from package `ratedit` to get two tables

```python
from rat.ratedit import roll_strong
df_family_strong, cols_family_strong = roll_strong(df_c, ['District'], ['Sex'], ['Single', 'Marriged', 'Widower'], value_name='Family status')
```
The first is interesting table with renamed columns:

```python
df_family_strong
```
| | District | col_0 | col_1 | col_2 | col_3 | col_4 | col_5 | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
| 0 | East Forests | 2545 | 1702 | 2248 | 2920 | 314 | 2044 |
| 1 | North Mountains | 3059 | 3207 | 3352 | 4578 | 617 | 2654 |

And the second is explanation of new column names:

```python
cols_family_strong
```
|       |      Sex | Family status | 
| --- | --- | --- |
| col_0 |   Female |     Single | 
| col_1 |   Female |   Marriged | 
| col_2 |   Female |    Widower | 
| col_3 |     Male |     Single | 
| col_4 |     Male |   Marriged | 
| col_5 |     Male |    Widower | 

You can change `index_prefix` parameter from default `'col_'` to any you like.


### Restoring alot of tables

If we want to restore many tables consistently (__employment__, __enviroment__ and __family__), we should edit them to same names columns and different value columns. 

In our case that is just change `df_family` to `df_family_strong`. So we have three tables (`df_employment`, `df_enviroment` and `df_family_strong`) with name-column __District__.

To restore them consistently, we can use `restore_alot` function from package `ratrestore`

```python
from rat.ratrestore import restore_alot

df_alot = restore_alot([df_employment, df_enviroment, df_family_strong], name_cols=['District']
                       tab_names=['Employment', 'Enviroment', 'Family'], name_res='Count')
df_alot.head(5)
```
| | District | Employment | Enviroment | Family | Count | 
| --- | --- | --- | --- | --- | --- |
| 0 | East Forests | Agriculture | Rural | col_0 | 242.319898 | 
| 1 | East Forests | Agriculture | Rural | col_1 | 162.054407 | 
| 2 | East Forests | Agriculture | Rural | col_2 | 214.041309 | 
| 3 | East Forests | Agriculture | Rural | col_3 | 278.025187 | 
| 4 | East Forests | Agriculture | Rural | col_4 | 29.897229 | 

But __Family__ column doess not look beautiful. So let do some not difficult actions:

```python
df_alot = df_alot.merge(cols_family_strong, how='left', left_on='Family', right_index=True)
df_alot = df_alot[np.concatenate([['District'], ['Employment', 'Enviroment'], cols_family_strong.columns, ['Count']])]
df_alot.head(5)
```
| | District | Employment | Enviroment | Sex | Family status | Count | 
| --- | --- | --- | --- | --- | --- | --- |
| 0 | East Forests | Agriculture | Rural | Female |     Single | 242.319898 | 
| 1 | East Forests | Agriculture | Rural | Female |   Marriged | 162.054407 | 
| 2 | East Forests | Agriculture | Rural | Female |    Widower | 214.041309 | 
| 3 | East Forests | Agriculture | Rural |   Male |     Single | 278.025187 | 
| 4 | East Forests | Agriculture | Rural |   Male |   Marriged | 29.897229 | 

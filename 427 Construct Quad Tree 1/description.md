## Construct Quad Tree

Topics: Divide and Conquer  
Complexidade: Medium  
ID: 427  
Link: https://leetcode.com/problems/construct-quad-tree/?envType=problem-list-v2&envId=divide-and-conquer

Dado a `n * n` matriz `grid` de `0's` e `1's` somente. Queremos representar `grid` com uma Quad-Tree.

Retorno _a raiz da Quad-Tree representando_ `grid`.

Uma Quad-Tree é uma estrutura de dados em árvore na qual cada nó interno tem exatamente quatro filhos. Além disso, cada nó possui dois atributos:

- `val`: Verdadeiro se o nó representa uma grade de 1 ou Falso se o nó representa uma grade de 0. Observe que você pode atribuir o `val` para Verdadeiro ou Falso quando `isLeaf` é falso e ambos são aceitos na resposta.
- `isLeaf`: Verdadeiro se o nó for um nó folha na árvore ou Falso se o nó tiver quatro filhos.

```
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}
```

Podemos construir uma Quad-Tree a partir de uma área bidimensional usando as seguintes etapas:

1. Se a grelha actual tiver o mesmo valor (ou seja, todos `1's` ou todos `0's`) conjunto `isLeaf` Verdadeiro e definido `val` para o valor da grade e definir as quatro crianças para Null e parar.
2. Se a grelha actual tiver valores diferentes, defina `isLeaf` para Falsear e definir `val` para qualquer valor e divida a grade atual em quatro sub-redes como mostrado na foto.
3. Recurse para cada uma das crianças com a sub-grade adequada.
   ![](https://assets.leetcode.com/uploads/2020/02/11/new_top.png)

If you want to know more about the Quad-Tree, you can refer to the [wiki](https://en.wikipedia.org/wiki/Quadtree).

**Quad-Tree format:**

You don't need to read this section for solving the problem. This is only if you want to understand the output format here. The output represents the serialized format of a Quad-Tree using level order traversal, where `null` signifies a path terminator where no node exists below.

It is very similar to the serialization of the binary tree. The only difference is that the node is represented as a list `[isLeaf, val]`.

If the value of `isLeaf` or `val` is True we represent it as **1** in the list `[isLeaf, val]` and if the value of `isLeaf` or `val` is False we represent it as **0**.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/02/11/grid1.png)

```
Input: grid = [[0,1],[1,0]]
Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
Explanation: The explanation of this example is shown below:
Notice that 0 represents False and 1 represents True in the photo representing the Quad-Tree.
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/02/12/e2mat.png)

```
Input: grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
Output: [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
Explanation: All values in the grid are not the same. We divide the grid into four sub-grids.
The topLeft, bottomLeft and bottomRight each has the same value.
O topRight tem valores diferentes, então dividimos em 4 sub-redes onde cada uma tem o mesmo valor.
A explicação é mostrada na foto abaixo:
```

**Restrições:**

- `n == grid.length == grid[i].length`
- `n == 2<sup>x</sup>` onde `0 <= x <= 6`

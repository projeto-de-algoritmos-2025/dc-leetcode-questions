## Construct Binary Tree from Preorder and Postorder Traversal

Topics: Divide and Conquer  
Complexidade: Medium  
ID: 889  
Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description/?envType=problem-list-v2&envId=divide-and-conquer

Dadas duas matrizes inteiras, preorder e postorder onde preorder é a pré-ordem de uma árvore binária de distinto valores e postorder é a travessia da mesma árvore, reconstrução e retorno a árvore binária.

Se houver várias respostas, você pode devolver qualquer deles.

Exemplo 1:

<img src="assets/lc-prepost.jpg" alt="lc prepost" width="320">

Entrada: pré-encomenda = [1,2,4,5,3,6,7], pós-encomenda = [4,5,2,6,7,3,1]
Saída: [1,2,3,4,5,6,7]

Exemplo 2:

Entrada: pré-encomenda = [1], pós-encomenda = [1]
Saída: [1]

Restrições:

- 1 <= preorder.length <= 30
- 1 <= preorder[i] <= preorder.length
- Todos os valores de preorder são único.
- postorder.length == preorder.length
- 1 <= postorder[i] <= postorder.length
- Todos os valores de postorder são único.
- É garantido que preorder e postorder são a travessia de pré-ordem e a travessia de pós-ordem da mesma árvore binária.

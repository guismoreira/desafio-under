# Desafio Under

## Problema 1

Dado um horário no formato AM/PM, converta-o para o formato 24 horas.
OBS:

12:00:00AM em um relógio de 12 horas é 00:00:00
12:00:00PM em um relógio de 12 horas é 12:00:00

Descrição:
Crie uma função para a conversão do tempo. Ela deve retornar uma nova string
representando a hora de entrada no formato de 24 horas.

Entrada:
Uma única string que representa uma hora no formato de 12 horas (ou seja:
hh:mm:ssAM ou hh:mm:ssPM).

Retorno:
Uma string que representa a hora no formato 24 horas.

## Problema 2

Dada uma matriz quadrada, calcule a diferença absoluta entre as somas de suas
diagonais.
Por exemplo, a matriz quadrada abaixo:

1 2 3
4 5 6
9 8 9

A diagonal que vem da esquerda para direita = 1 + 5 + 9 = 15. A diagonal que vem
da direita para esquerda = 3 + 5 + 9 = 17. E sua diferença absoluta é |15 - 17| = 2

Descrição:
Crie uma função para calcular a diferença absoluta das diagonais.

Entrada: Uma matriz quadrada de números inteiros.

Saída: A diferença absoluta entre as somas das duas diagonais da matriz como um
único inteiro.

## Problema 3

Você recebe uma lista de n inteiros, ar = [ar[0], ar[1], ..., ar[n-1]] ,e um inteiro positivo, k.
Encontre e imprima o número de pares (i,j) onde i < j e ar[i] + ar[j] é divisível por k.
Por exemplo, ar=[1, 2, 3, 4, 5, 6] e k=5. Nossos três pares que atendem aos critérios são
[1,4], [2,3] e [4,6].

Descrição:
Crie uma função que deve retornar a contagem inteira de pares que atendem aos critérios.

Entrada:
ar: uma lista de inteiros positivos
k : o inteiro positivo para dividir a soma do par

Ex:
ar = [1, 3 , 2, 6, 1, 2]
k = 3

Saída: Imprimir o número de pares (i,j) onde i < j e a[i] + a[j] e é divisível por k.
Ex: 5

Exemplo:

Entradas:
ar = [1, 3 , 2, 6, 1, 2]
k = 3

Saída: 5
Explicação

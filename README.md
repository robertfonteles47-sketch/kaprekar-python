 Algoritmo de Kaprekar (6174)

Este projeto implementa, em Python, o processo de Kaprekar para números de 4 dígitos, demonstrando passo a passo como alcançar a constante 6174.

 Sobre o problema

O processo de Kaprekar consiste em:

Pegar um número de 4 dígitos (com pelo menos dois dígitos diferentes)
Formar:
O maior número possível com seus dígitos
O menor número possível com seus dígitos

Subtrair:

maior - menor

Repetir o processo com o resultado

 Independentemente do número inicial (com algumas restrições), o resultado sempre converge para:

 6174 (Constante de Kaprekar)

Funcionalidades

Validação de entrada (número positivo de até 4 dígitos)
Verificação de dígitos repetidos
Execução passo a passo do algoritmo
Exibição detalhada de cada iteração
Contagem total de passos até chegar em 6174

 Como executar
 
Certifique-se de ter o Python instalado
Execute o arquivo:
python kaprekar.py
Digite um número de 4 dígitos quando solicitado

Exemplo de execução

Entrada:

3524

Saída:

Passo 1 : 5 4 3 2 - 2 3 4 5 = 3 0 8 7

Passo 2 :
Constante
6174 alcançada em X passos.

 Restrições
 
O número deve estar entre 0000 e 9999
Não pode ter 3 ou mais dígitos iguais

 Objetivo do projeto

Este projeto foi desenvolvido com fins acadêmicos para praticar:

Estruturas de repetição
Condicionais
Manipulação matemática de números
Lógica de programação

Autor

Desenvolvido por: Robert Fonteles Martins

 Observação

O código foi implementado sem uso de manipulação de strings, trabalhando apenas com operações matemáticas, conforme restrições da atividade.

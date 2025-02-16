Este repositório apresenta um Gerador e Verificador de CPF em Python. O programa permite ao usuário gerar um CPF válido aleatoriamente ou verificar se um CPF fornecido manualmente é válido.

📁Estrutura do código:
importação de bibliotecas:
- RANDOM (Gera números aleatórios escolhidos entre 0 a 9);
- OS (Permite executar o comando "cls" para limpeza do terminal);
- RE (Utilizado para excluir pontos e hífen do CPF).

📱 Cálculo dos dígitos verificadores:
- Cria 9 números aleatorios entre 0 e 9, utilizando a biblioteca RANDOM.
- Para o primeiro digito é necessário multiplicar cada um dos 9 valores do CPF por uma contagem regressiva começando de 10 até 2, somando todos os resultados e multiplicando por 10 e obtendo o resto da divisão da conta anterior por 11.
- Para o segundo digito é necessário a soma dos 9 primeiros dígitos do CPF mais o valor do primeiro digito, multiplicando cada um dos valores por uma contagem regressiva começando de 10, somando todos os resultados e multiplicando por 10 e obtendo o resto da divisão da conta anterior por 11.
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

🔧 Execução do programa:


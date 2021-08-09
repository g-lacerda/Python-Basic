import math
print ('_' * 20)
escolha = int(input('Escolha o que você quer abrir:\n 1. Calcular bhaskara \n 2. Tabuada \n 3. Conversor de moedas \n 4. Dissecar váriável \n 5. Calcular média \n 6. Calcular desconto \n 7. Calcular aumento salarial \n 8. Calcular seno, cosseno e tangente do ângulo \n       -->'))

while (escolha < 1):
    escolha = int(input('Por favor, insira uma opção válida: '))
    while (escolha > 8):
        escolha = int(input('Por favor, insira uma opção válida: '))

while (escolha > 8):
    escolha = int(input('Por favor, insira uma opção válida: '))
    while (escolha < 1):
        escolha = int(input('Por favor, insira uma opção válida: '))

if escolha == 1:
    print ('_' * 20)
    print ('Calculadora de Bhaskara')

    a = float(input('Digite o valor de A: '))
    b = float(input('Digite o valor de B: '))
    c = float(input('Digite o valor de C: '))

    delta = (b ** 2) - 4 * a * c

    if a == 0:
        print (' O valor de A deve ser diferente de 0')
    elif delta < 0:
        print ('Delta não pode ser negativo')
    else:
        X1 = (-b + delta ** (1 / 2)) / (2 * a)
        X2 = (-b - delta ** (1 / 2)) / (2 * a)
        print('O resultado de delta será {}'.format(delta ** 2))
        print('O resultado de X1 será {}'.format(X1))
        print('O resultado de X2 será {}'.format(X2))
        print('_' * 20)

elif escolha == 2:

    print('_' * 20)
    n = int(input('Digite algum número: '))
    m = 1
    for m in range(1, 11):
        print('{:2} x {} = {}'.format(n, m, n * m))
        m = m + 1
    print ('_' * 20)

elif escolha == 3:

    print('_' * 20)
    print('Os valores foram atualizados da última vez em: 04/08/2021, as 03:10')
    n = float(input('Quantos reais você tem? R$'))
    print ('Com seus R${} (reais), você consegue ter U${:.2f} (dólares)'.format(n, n / 5.20))
    print ('Com seus R${} (reais), você consegue ter €{:.2f} (euros)'.format(n, n / 6.17))
    print ('Com seus R${} (reais), você consegue ter £{:.2f} (libras)'.format(n, n / 7.24))
    print ('Com seus R${} (reais), você consegue ter ¥{:.2f} (ienes)'.format(n, n / 0.048))
    print('_' * 20)

elif escolha == 4:

    print('_' * 20)
    algo = input('Digite algo: ')
    print ('O tipo primitivo disto é: ', type(algo))
    print ('É alfanumérico?', algo.isalnum())
    print ('É alfabético?', algo.isalpha())
    print ('É ascii?', algo.isascii())
    print ('É digíto?', algo.isdigit())
    print ('É minúsculo?', algo.islower())
    print ('É decimal?', algo.isdecimal())
    print ('É identificador?', algo.isidentifier())
    print ('É numérico?', algo.isnumeric())
    print ('É printável?', algo.isprintable())
    print ('Só tem espaços?', algo.isspace())
    print ('É capitalizado?', algo.istitle())
    print ('É maiúsculo?', algo.isupper())
    print ('_'*20)

elif escolha == 5:

    n1 = float(input('Qual o primeiro valor? '))
    n2 = float(input('Qual o segundo valor? '))

    soma = n1 + n2
    divisao = 2

    while (True):
        a = int(input('Deseja adicionar mais algum valor?\n 1. SIM\n 2. NÃO\n  -->'))
        if a == 1:
            n3 = float(input('Qual valor? '))
            soma = soma + n3
            divisao = divisao + 1

        elif a == 2:
            print('Você tem uma média de {:.2f}'.format((soma) / divisao))
            print('_' * 20)
            break

        else:
            print('Insira uma resposta válida.')

elif escolha == 6:

    print('_' * 20)
    n = float(input('Qual o valor do produto? R$'))
    d = int(input('Qual a porcentagem de desconto? '))
    print('O valor do seu produto com {}% de desconto, será de R${}'.format(d, n / 100 * (100 - d)))
    print('_' * 20)

elif escolha == 7:
    print('_' * 20)
    n = float(input('Qual o seu salário atualmente? R$'))
    a = int(input('Qual será o aumento do seu salário em porcentagem? '))
    print('Seu salário irá aumentar R${}, totalizando R${:.2f} mensais'.format(n / 100 * a, n / 100 * (100 + a)))
    print('_' * 20)

elif escolha == 8:
    n = float(input('Insira o ângulo: '))
    while (n == 90):
        print('O valor deve ser diferente de 90 graus')
        n = float(input('Insira o ângulo: '))
    print('Os valores do ângulo {} são:\nSeno:{:.2f}\nCosseno:{:.2f}\nTangente:{:.2f}'.format(n,
                                                                                              math.sin(math.radians(n)),
                                                                                              math.cos(math.radians(n)),
                                                                                              math.tan(
                                                                                                  math.radians(n))))

else:
    print ('Erro')




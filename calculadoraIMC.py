# desenvolva uma calculadora de IMC, o programa deve pedir o peso e
# a altura ao usuario. calcular o IMC e retornar para o usuario o IMC
#e a categoria em que se encontra

# menor que 18,5 - abaixo do peso
# entre 18,5 e 24,9 - peso normal
# entre 25 e 29,9 - sobrepeso
# igual ou acima de 30 - obesidade


def calcular_imc():
    altura = float(valor_altura())
    peso = float(valor_peso())

    imc = peso / altura**2

    resultado['text'] = ('seu IMC é:',imc)

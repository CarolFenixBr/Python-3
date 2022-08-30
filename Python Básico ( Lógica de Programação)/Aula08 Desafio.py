"""
☑Criar variáveis para nome (str), idade(int)
☑altura (float) e peso (float) de uma pessoa
☑Criar variável com o ano atual (int)
☑Obter o ano de nascimento da pessoa ( baseado na idade e no ano atual)
☑Obter o IMC da pessoa com 2 casas decimais( peso e na altura da pessoa)
☑Exibir um texto com todos os valores na tela usando F-Strings( com as chaves)
"""

nome = 'Caroline'
idade = 29
altura = 1.63
peso = 58.7
ano_atual= 2022
ano_nascimento= ano_atual - idade
imc = peso/ altura **2

print('{} tem {} anos de idade com altura {} e peso {} nasceu em {} e possui o IMC de {:.2f}'.format(nome,idade,altura,peso,ano_nascimento,imc))

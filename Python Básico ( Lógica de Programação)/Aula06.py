"""
Iniciar com letra, pode conter números, separar _, letra minúsculas
"""
nome = 'Caroline'
idade = 28  #int
altura= 1.63 #float
e_maior = idade >18 #bool
peso = 58
data_atual = 2022
imc = peso / altura **2

print('Nome', nome)
print('Idade', idade)
print('Altura', altura)
print('É maior:', e_maior)
print('Peso:', peso)
print('Data:', data_atual)

print(nome, 'tem', idade,'anos de idade e seu imc é', imc)

salario= float(input("informe o seu salário"))
               
if salario < 128000:
    percentagem = 0.2
    aumento = salario*percentagem
    novo_salario = salario + aumento
elif(salario >=128000 and salario <=500000):
    percentagem = 0.15
    aumento = salario*percentagem
    novo_salario= salario+aumento
elif(salario >=500000 and salario<=100000000):
    percentagem = 0.1
    aumento = salario*percentagem
    novo_salario= salario+aumento
else:
    percentagem=0.05
    aumento= salario*percentagem
    novo_salario= salario+aumento
print("salario antes de reajuste:",salario)
print("percentagem:", percentagem)
print( "aumento a ser aplicado:", aumento)
print("Novo salario:" ,novo_salario)
    
    

            

print("--- Hospital xxx ---")
print("Seja bem vindo!")

nome = input("Qual o seu nome? ")
idade = float (input("Qual a sua idade? "))

if idade < 15 or idade > 60:
    print("Atendimento prioritario!!")
else:
    prior = input("Você tem histórico de outras doenças de risco? (Cancer/etc..) [S/N]")
    prior = prior.upper()
    if prior == "S":
        print("Atendimento prioritario!!")
    else:
        print("Segue na fila")


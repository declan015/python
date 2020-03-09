print("--- Sistema xxx ---")
print("Seja bem vindo!")
gen = "z"
cargo = "z"
nome = input("Qual o seu nome? ")

while (gen != "MASC" and gen != "FEM"):
    gen = input("Qual o seu sexo? [masc/fem] ").upper()


while (cargo != "ADM" and cargo != "USR" and cargo != "GUEST"):
    cargo = input("Qual o seu cargo? [adm/usr/guest/null] ").upper()

if gen == "MASC":
    if cargo == "ADM":
        print("Seja bem vindo administrador " + nome)
    elif cargo == "USR":
        print("Seja bem vindo usuario " + nome)
    elif cargo == "GUEST":
        print("Seja bem vindo visitante " + nome)
    else:
        print("Seja bem vindo desconhecido")
    
else:
    if cargo == "ADM":
        print("Seja bem vinda administradora " + nome)
    elif cargo == "USR":
        print("Seja bem vinda usuaria " + nome)
    elif cargo == "GUEST":
        print("Seja bem vinda visitante " + nome)
    else:
        print("Seja bem vinda desconhecida")



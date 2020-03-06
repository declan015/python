nota1 = float (input("Digite a primeira nota: "))
nota2 = float (input("Digite a segunda nota: "))

media = (nota1+nota2)/2


if media >= 6:
    print("Você foi aprovado!")
    print("Sua média foi de: " + str (media))
elif media < 4:
    print("Você foi reprovado")
    print("Sua média foi de: " + str (media))
else:
    print("Você ficou de exame!")
    print("Sua média foi de: " + str (media))
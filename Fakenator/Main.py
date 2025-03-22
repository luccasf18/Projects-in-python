import random

frase = input("tente advinhar o numero de 0 a 10 em 3 tentativas, você aceita? (S/N): ")
contador = 0

if frase == "S" or frase == "s":
    numberRandom = random.randint(0, 10)
    

    while contador < 3:
      number = int(input("Digite um numero de 0 a 10: "))
      

      if number == numberRandom:
         print("Parabens!!, Voce acertou")
         break
      elif contador == 2:
         print("Nao foi dessa vez, tente novamente mais tarde!")
         break
      else:
         print("Tente novamente!!!")

      contador = contador + 1
    

elif frase == "N" or frase == "n":
    print("Que pena que não quis brincar, :( ")
else:
    print("valor errado")
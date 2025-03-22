salario = float(input("Diga o salario : \n-> R$ "))

if salario <= 1900.98 : 
    print("Isento")
elif salario >= 1900.98 and salario <= 2826.65:
    print(f"o valor de desconto é de (7.5%): R$ {salario * 0.075}")
elif salario >= 2826.66 and salario <= 3751.05:
    print(f"o valor de desconto é de (15%): R$ {salario * 0.15}")




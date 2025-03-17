
num_a = float(input("Digite um número: "))
num_b = float(input("diga outro numero: "))
operation = input("diga a operação ( +,-,*,/ ): ")

if operation == "+":
    calc = num_a + num_b
elif operation == "-":
    calc = num_a - num_b
elif operation == "*":
    calc = num_a * num_b
elif operation == "/":
    calc = num_a / num_b

print(calc)
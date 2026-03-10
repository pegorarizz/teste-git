while True:
    try:
        numero = int(input("Digite um número: "))
        break
    except ValueError:
        print("Você digitou algo inválido. Digite apenas números.")
        
print(numero + 2)
while True:
    try:
        n = int(input("Digite um número para calcular o fatorial: "))
        break
    except ValueError:
        print("Digite apenas números.")

fatorial = 1

for i in range(1, n + 1):
    fatorial *= i

print(f"O fatorial de {n} é {fatorial}")
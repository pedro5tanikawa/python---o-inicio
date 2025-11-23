contador = 0
entre = 0

while contador < 15:
    num = int(input('Digite um número: '))
    
    if num > 10 or num < 20:
        entre += 1
    
    contador += 1

print(f"Quantidade de números entre 10 e 20: {entre}")

'''
    Dada a lista nums = [1, 2, 3, 4, 5, 6, 7, 8], crie uma nova lista somente com os números ímpares. 
'''

nums = [1, 2, 3, 4, 5, 6, 7, 8]
impares = []
for n in nums:
    if n % 2 != 0:
        impares.append(n)

print(nums)
print(impares)
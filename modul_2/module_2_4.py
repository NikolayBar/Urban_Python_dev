numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for i in numbers:
    count = 0
    if i == 1:
        continue
    for j in range(2, i // 2 + 1):
        count += 1 if i % j == 0 else 0
        if count > 0:
            break
    if count:
        not_primes.append(i)
    else:
        primes.append(i)

print(f'Primes: {primes}')
print(f'Not Primes: {not_primes}')
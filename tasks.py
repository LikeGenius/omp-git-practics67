# Задачи пары: раунд 2 — fizzbuzz, раунд 3 — is_prime.

# Вместо ... впишите своё имя, вместо raise NotImplementedError — решение.
# Проверить, что файл запускается без ошибок: python3 tasks.py



def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

# Реализовал Дмитрий Караулов

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        d = set()
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    if len(d) == 0:
        return True
    else:
        return False

# Реализовал Дмитрий Караулов

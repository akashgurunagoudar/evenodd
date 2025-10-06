

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))


odd_count = 0
even_count = 0
prime_count = 0


for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    if is_prime(num):
        prime_count += 1


print(f"\nTotal numbers entered: {len(numbers)}")
print(f"Even numbers count: {even_count}")
print(f"Odd numbers count: {odd_count}")
print(f"Prime numbers count: {prime_count}")

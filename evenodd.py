user_input = input("Enter numbers separated by spaces: ")

numbers = list(map(int, user_input.split()))

odd_count = 0
even_count = 0


for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1


print(f"\nTotal numbers entered: {len(numbers)}")
print(f"Even numbers count: {even_count}")
print(f"Odd numbers count: {odd_count}")

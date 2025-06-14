numbers=[1, 2, 3, 4, 3,5, 1, 2, 3, 6, 7, 8, 9]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print(unique_numbers)
print("Length of unique numbers:", len(unique_numbers))
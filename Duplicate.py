numbers = [1, 2, 3, 2, 4, 5, 1]

seen = set()

for num in numbers:
    if num in seen:
        print(num)
    else:
        seen.add(num)

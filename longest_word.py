words = ["cat", "elephant", "dog", "tiger"]

longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print(longest)

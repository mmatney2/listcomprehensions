#Dict list comp: {new_key : new_value for element in iterable if}

#create a dictionary of letters of keys and the number of time letter appears

# 'coding temple' -> {c:0, o:1}
letters = {}
animal = 'fennec fox'
for char in animal:
    if char != ' ':
        letters[char] = animal.count(char)
print(letters)

letters2 = {char: animal.count(char) for char in animal if char != ' '}
print(letters2)
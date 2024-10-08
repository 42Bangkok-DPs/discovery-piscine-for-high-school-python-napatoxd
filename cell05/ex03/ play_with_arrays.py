array = [2, 8, 9, 48, 8, 22, -12, 2]

unumbers = set(array)

new = {num + 2 for num in unumbers if num > 5}

print(array)  
print(new)       

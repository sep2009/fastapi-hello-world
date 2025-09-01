colors = ['red', 'blue', 'green']
numbers = [4, 8, 23, 56, 2]
colors_2 = ['white', 'black']


 colors.extend(colors_2)
print(colors)
all_colors.pop()
print(colors)

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

print('green' in colors)
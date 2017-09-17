numbers = [1, 2, 3, 4, 5, 6, 7]
even = []
odd = []
while len(numbers) > 0:
    number = numbers.pop()
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)


fruits = ["apple", "orange", "banana"]
for index in range(len(fruits)):
    print fruits[index]

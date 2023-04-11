# 1-D list
numbers = list(range(20, 31))

total = sum(numbers)
average = total / len(numbers)

print("Numbers:", numbers)
print("Sum:", total)
print("Average:", str(average) + "\n")

num_27 = numbers[numbers.index(27)]
print("Retrieving the lucky number:", num_27)
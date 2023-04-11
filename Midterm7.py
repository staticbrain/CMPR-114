# 2-D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]

print("2-D list:")
for sublist in matrix:
    print(sublist)

# Retrieve the lucky number 7
luckyNum = None

for sublist in matrix:
    if 7 in sublist:
        luckyNum = sublist[sublist.index(7)]
        break

if luckyNum:
    print("\nLucky number 7 found in the 2-D list.")
    
else:
    print("\nLucky number 7 not found in the 2-D list.")
    
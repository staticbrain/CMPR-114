def write():
    
    categories = ['Rent', 'Gas', 'Food', 'Clothing', 'Car Payment']

    with open('C:\\Users\\0cher\\Downloads\\Expenses.txt', 'w') as file:
        
        #for loop used to ask for each category
        for category in categories:
            
            expense = input("Enter expense for {}: $".format(category))
            file.write("{}: ${}\n".format(category, expense))

    print("Expenses written to file.\n")


def read():
    
    inFile = open('C:\\Users\\0cher\\Downloads\\Expenses.txt', 'r')

    fileContents = inFile.read()

    inFile.close()

    print(fileContents)



write()
read()

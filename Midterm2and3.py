
def read():
    inFile = open('C:\\Users\\0cher\\Downloads\\Coffee.txt', 'r')

    fileContents = inFile.read()

    inFile.close()

    print(fileContents)

read()

def write():
    prodNum = "99-8888"
    price = float(9.88)

    favCoffee = input("\nPlease enter your favorite coffee brand: ")

    outFile = open('C:\\Users\\0cher\\Downloads\\Coffee.txt', 'a')

    outFile.write(favCoffee + ", " + prodNum + ", " + str(price))

    outFile.close()

    print("Your favorite coffee brand has been added. \n")

write()

read()
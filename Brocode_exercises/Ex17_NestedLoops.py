#Nested loops

rows = int(input("Enter the rows:\n"))
columns= int(input("Enter the columns:\n"))
symbol = input("Enter the symbols:")
for i in range(rows):
    for j in range(columns):
        print(symbol,end="")
    print()
for x in range(10):
    for y in range(x):
        print("*", end=' ')
    print()  #newline
print("\n New Shape \n")


for x in range(10):
    ast="*"
    #print(ast)
    for x in range(20):
        print(ast, end='')
    print()
print("\n New Shape \n")

ast="*"
for x in range(10):
    for y in range(10-x):
        print(" ", end = '')
    print(ast)
    ast+="**"
print("\n New Shape \n")

for x in range(10):
    ast="*"
    #print(ast)
    for x in range(20):
        print(ast, end=' ')
    print()
print("\n New Shape \n")


for x in range(10):
    ast="*"
    for y in range(10-x):
        print(" ", end = '')
    print(ast)
print("\n New Shape \n")


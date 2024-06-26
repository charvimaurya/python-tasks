#print a list of even numbers
x=int(input("please enter a number:"))
for x in range (2,x+2):
    if x%2 == 0:
        print(x)
    else:
        continue
#print a list of odd numbers
x=int(input("please enter a number:"))
for x in range (1,x+1):
    if x%2 != 0:
        print(x)
    else:
        continue
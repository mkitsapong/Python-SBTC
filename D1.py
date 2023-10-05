PI = 3.1416 

def addition(*args):
    total = 0
    for i in range(len(args)):
        total+=args[i]
    print("ผลบวก = ", total)

def subtraction(num1, num2):
    print("ผลลบ = ",(num1 - num2))        
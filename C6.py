number = int(input("ป้อนขนาด :"))

for row in range(number):
    for column in range(number):
        if (row+column)%2==0:
            print("X",end="")
        else:
            print("0",end="")
    print(" ")    
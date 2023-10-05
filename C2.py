sum = 0

while True:
    number=int(input("ป้อนตัวเลข :"))
    sum+=number
    if sum>=100:
        break
print("ผลรวม =",sum)
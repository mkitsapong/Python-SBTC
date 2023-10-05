data = {"200":"ต้มยำกุ้ง" , "40": "ผัดกะเพรา" , "35": "ไก่กระเทียม" , "30": "ข้าวมันไก่" , "30": "ไข่เจียว" , "30": "ผัดไทย"}
def searchNumber(message):
    for key, value in data.items():
        if value == message:
            print("ราคา : ", key)
            break
    else:
            print("ไม่มีข้อมูล")
            return
message = input("ป้อนอาหารที่ต้องการ = ")
searchNumber(message)
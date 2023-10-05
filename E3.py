import qrcode

def basic():
    txt = "https://www.naiin.com/?fbclid=IwAR3oAJJoTxejq3ceEvI5My6fIThEVV4ZfQtbuD_VrnlpM79mcxi8yhB2WV0"
    img = qrcode.make(txt)
    img.show()
if __name__=="__main__":
    basic()

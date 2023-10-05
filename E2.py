import matplotlib.pyplot as plt

def demo():
    x=range(2014, 2021)
    y=(19, 25, 18, 22, 10, 28, 22)
    plt.plot(x[:4],y[:4], color="black", label="for-test1")
    plt.plot(x[3:],y[3:], color="black", linestyle="--", label="for-test")
    plt.title("Test")
    plt.ylabel("unit")
    plt.xlabel("year")
    plt.legend()
    plt.show()

if __name__=="__main__":
    demo()    
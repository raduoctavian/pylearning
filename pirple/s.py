""" import signal

s = signal.valid_signals()

print(s) """

a = 0.1
b = 0.2
c = -0.3

x = a + b
#print(x)

def myF(x, y, z):
    return x + y - z

rezult = myF(1.1, 2.2, 3.2)
print(rezult)

rezult2 = myF(1.1, 2.2, 3.3)
print(rezult2)
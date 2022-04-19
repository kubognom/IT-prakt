import numpy as np


class trig:
    def __init__(self,chislo):
        self.chislo = chislo

    def cos(self):
        print(np.cos(self.chislo))

    def sin(self):
        print(np.sin(self.chislo))

    def tan(self):
        print(np.tan(self.chislo))

    def asin(self):
        print(np.asin(self.chislo))

    def acos(self):
        print(np.acos(self.chislo))

    def atan(self):
        print(np.atan(self.chislo))

    def to_rad(self):
        print(self.chislo * np.pi / 180)
q=0
trig1 = trig(int(input("Введите число >> ")))
while q!=8:
    q = int(input("1-cos 2-sin 3-tan 4-asin 5-acos 6-atan 7-to rad >> "))
    if q==7:
        trig1.to_rad()
    if q==6:
        trig1.atan()
    if q==5:
        trig1.acos()
    if q==4:
        trig1.asin()
    if q==3:
        trig1.tan()
    if q==2:
        trig1.sin()
    if q==1:
        trig1.cos()

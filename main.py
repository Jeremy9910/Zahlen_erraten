from ast import While
from distutils import dist
import random
import math
from typing_extensions import Self
class Zahlen_erraten:

    def __init__(self):
        self.b = random.randint(1,100)
        print('Du hast 3 Versuche')

    def raten(self, ):    
        for i in range(3):
            self.a = int(input("geben sie eine Zahl zwischen 1 und 100 ein"))
            self.dist = self.a - self.b   
            
            print(f'{i + 1}.Versuch')
            if self.a == self.b:
                print("Du hast die Zahl erkannt")
                break
            elif self.a != self.b:
                if self.dist < 0:
                    self.dist = - self.dist
                print(f'Abstand ist {self.dist}')
                self.__init__
            i += 1
g = Zahlen_erraten()
g.raten()



            


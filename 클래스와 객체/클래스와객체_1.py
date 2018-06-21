#접근자와 설정자 도전문제 1
class Circle() :
    from math import pi
    def __init__(self,radius=0.0):
        self.__radius=radius

    def getRadius(self):
        return self.__radius

    def setRadius(self,radius=0.0):
        if radius<=0.0 :
            self.__radius = 0.0
        else:
            self.__radius=radius

    def getSpace(self):
        result
        return pi*(self.__radius**2)

    def getLength(self):
        return 2*pi*(self.__radius)

    def __str__(self):
        result="원의 반지름은 "+self.__radius


a=Circle(10)


#Liu Pei Jou
#ITP 115 Spring 2017
#5/9/2017
#peijouli@usc.edu
#Menu Item


class MenuItem(object):
    def __init__(self, name, type, price, description):
        self.__name = name
        self.__type = type
        self.__price = price
        self.__description = description

    def getName(self):
       return self.__name

    def setName(self, newName):
       self.__name = newName

    def getType(self):
       return self.__type

    def setType(self,newType):
        self.__type = newType

    def getPrice(self):
        return self.__price

    def setPrice(self, newPrice):
            self.__price = newPrice

    def getDescription(self):
        return self.__description

    def setDescription(self, newDiscription):
            self.__description = newDiscription.strip()

    #str method
    def __str__(self):
        msg = self.__name + "(" + self.__type + "):"
        msg += "$" + str(self.__price)
        msg += " " +self.__description
        return msg
#Liu Pei Jou
#ITP 115 Spring 2017
#5/9/2017
#peijouli@usc.edu
#Diner class

from MenuItem import MenuItem

class Diner(object):
    STATUSES=["seated", "ordering", "eating", "paying", "leaving"]
    def __init__(self, name):
        self.__name = name
        self.__order =[]
        self.__status = 0

    def getName(self):
        return self.__name

    def setName(self, newName):
        self.__name = newName

    def getOrder(self):
        return self.__order

    def setOrder(self,newOrder):
        self.__order = newOrder

    def getStatus(self):
        return self.__status

    def setStatus(self, newStatus):
        self.__status = newStatus

    def addToOrder(self, MenuItem):
        self.__order.append(MenuItem)

    def updateStatus(self):
        if self.__status <= 3:
            self.__status = self.__status + 1

    def printOrder(self):
        for item in self.__order:
            print(item)

    def calculateMealCost(self):
        totalCost = 0
        for item in self.__order:
            totalCost += item.getPrice()
        return totalCost

    def __str__(self):
        msg = "diner "
        msg += self.__name
        msg += " is currently "
        msg += Diner.STATUSES[self.__status]
        return msg


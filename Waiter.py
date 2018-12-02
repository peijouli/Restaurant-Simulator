from Menu import Menu
from Diner import Diner

#class waiter
class Waiter(object):
    def __init__(self, menu):
        self.__diners = []
        self.__menu = menu

    # Add the new Diner object to the waiter’s list of diners.
    def addDiner(self, diner):
        self.__diners.append(diner)

    #get
    def getNumDiners(self):
        return len(self.__diners)
    #length of the diner list

    #Print all the diners the waiter is keeping track of, grouped by their statuses
    def printDinerStatuses(self):
        for status in Diner.STATUSES:
            print("Diners who are " + status + ":")
            for diner in self.__diners:
                if Diner.STATUSES[diner.getStatus()] == status:
                    print(diner)
    #take order
    def takeOrders(self):
        for diner in self.__diners:
            if Diner.STATUSES[diner.getStatus()]== "ordering":
                menuTypes = []
                for type in Menu.MENU_ITEM_TYPE:
                    self.__menu.printMenuItemsByType(type)
                    ask=int(input("Please choose an item type"))

                    while ask < 0 or ask >= self.__menu.getNumMenuItemsByType(type):
                        ask = int(input("ERROR: Please choose an item type"))
                    newItem=self.__menu.getMenuItem(type,ask)
                    menuTypes.append(newItem)

                    diner.addToOrder(newItem)
                    print(diner.getName() + " ordered: ")
                    diner.printOrder()

    #For each diner that is paying, calculate the diner’s meal cost and print it
    # out in a message to the diner.
    def ringUpDiners(self):
        for diner in self.__diners:
            if Diner.STATUSES[diner.getStatus()]== "paying":
                print(diner.getName() + " needs to pay " + str(diner.calculateMealCost()))

    #remove diner after they are done
    def removeDoneDiners(self):
        dinerRemoved = []
        for diner in self.__diners:
            if Diner.STATUSES[diner.getStatus()] == "leaving":
                dinerRemoved.append(diner)
                print(diner.getName() + " thank you for visiting!")

        for diner in dinerRemoved:
            self.__diners.remove(diner)

# advance diners
    def advanceDiners(self):
        self.printDinerStatuses()
        self.takeOrders()
        self.ringUpDiners()
        self.removeDoneDiners()
        for diner in self.__diners:
            diner.updateStatus()


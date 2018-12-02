#Liu Pei Jou
#ITP 115 Spring 2017
#5/9/2017
#peijouli@usc.edu
#Menu Class

from MenuItem import MenuItem

#class menu
class Menu(MenuItem):
    MENU_ITEM_TYPE=["Drink", "Appetizer", "Entree", "Dessert"]
    def __init__(self,fileName):
        self.__menuItemDictionary= {Menu.MENU_ITEM_TYPE[0]:[],
              Menu.MENU_ITEM_TYPE[1]:[],
              Menu.MENU_ITEM_TYPE[2]:[],
              Menu.MENU_ITEM_TYPE[3]:[]}

        #open
        fileIn = open(fileName,"r")

        #create a list
        lineList = []

        #read file
        for line in fileIn:
            line=line.strip()
            lineList = line.split(",")
            menuItem = MenuItem(lineList[0], lineList[1], float(lineList[2]), lineList[3])

            self.__menuItemDictionary[lineList[1]].append(menuItem)
        fileIn.close()

#get Menu Item
    def getMenuItem(self,type,index):
        menu2 = self.__menuItemDictionary[type]
        return menu2[index -1]

#print menu item
    def printMenuItemsByType(self,type):
        print("----" + type + "----")
        for index in range (0, len(self.__menuItemDictionary[type])):
            print(str(index) + ")" + str(self.__menuItemDictionary[type][index]))

#get num menu items by type
    def getNumMenuItemsByType(self,type):
        return len(self.__menuItemDictionary[type])




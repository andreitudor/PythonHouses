from .house import House

class City:
  def __init__(self):
    self.first = House(0)
    self.last = House(0)
    self.first.rightNeighbor = self.last
    self.last.leftNeighbor = self.first
    #set them to 0 as they never change
    self.first.beforeDay = 0
    self.last.beforeDay = 0
    self.size = 2

  def buyHouse(self, day):
    house = House(day)
    beforeLast = self.last.leftNeighbor
    house.leftNeighbor = beforeLast
    house.rightNeighbor = self.last
    beforeLast.rightNeighbor = house
    self.last.leftNeighbor = house
    self.size += 1

  def inorder(self):
    self._inorder(self.first)

  def _inorder(self, house):
    print(house.day,  end = " ")
    if house.leftNeighbor is not None:
      print("link left", house.leftNeighbor.day, end = " ")
    if house.rightNeighbor is not None:
      print("link right", house.rightNeighbor.day, end = " ")
      print()
      self._inorder(house.rightNeighbor)
  
  def checkActivity(self):
    #skip first neighbor as always 0
    self._checkActivity(self.first.rightNeighbor)
  
  def _checkActivity(self, node):
    if node.leftNeighbor.beforeDay == node.rightNeighbor.day:
      node.day = 0
    else:
      node.day = 1
    if node.rightNeighbor is not None:
      self._checkActivity(node.rightNeighbor)
      
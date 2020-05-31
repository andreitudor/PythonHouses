from .house import House

class Neighborhood:
  def __init__(self):
    self.houses = []

  def buyHouse(self, data):
    house = House(data)
    if len(self.houses):
      leftNode = self.houses[len(self.houses)-1]
      house.leftNeighbor = leftNode
      leftNode.rightNeighbor = house
      self.houses.append(house)
    else:
      self.houses.append(house)

  def inorder(self):
    for house in self.houses:
      print(house.data,  end = " ")
      if house.leftNeighbor is not None:
        print("link left", house.leftNeighbor.data, end = " ")
      if house.rightNeighbor is not None:
        print("link right", house.rightNeighbor.data, end = " ")
      print()
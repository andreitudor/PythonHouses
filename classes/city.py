from .house import House

class City:
  def __init__(self):
    self.houses = []
    #append first and last houses
    self.houses.append(House(0))
    self.houses[0].beforeDay = 0
    self.houses.append(House(0))
    self.houses[1].beforeDay = 0

  def buyHouse(self, day):
    lastHouse = self.houses.pop()
    self.houses.append(House(day))
    self.houses.append(lastHouse)

  def inorder(self):
    states = []
    for i in range(1,len(self.houses) - 1):
      states.append(self.houses[i].day)
    return states

  def checkActivity(self):
    #skip first and last houses
    for i in range(1,len(self.houses)-1):
      if self.houses[i-1].beforeDay == self.houses[i+1].day:
        self.houses[i].beforeDay = self.houses[i].day
        self.houses[i].day = 0
      else:
        self.houses[i].beforeDay = self.houses[i].day
        self.houses[i].day = 1
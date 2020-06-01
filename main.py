from classes.city import City

list1 = [1, 0, 0, 0, 0, 1, 0, 0]
list2 = []

city = City()

for state in list1:
  city.buyHouse(state)

city.inorder()
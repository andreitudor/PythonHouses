from classes.city import City

list1 = [1, 0, 0, 0, 0, 1, 0, 0]
list2 = [1, 1, 1, 0, 1, 1, 1, 1]

city = City()

for state in list1:
  city.buyHouse(state)
print(city.inorder())
for i in range(1, 2):
  city.checkActivity()

print(city.inorder())

city2 = City()

for state in list2:
  city2.buyHouse(state)
print(city2.inorder())
for i in range(1, 3):
  city2.checkActivity()

print(city2.inorder())
import math
def circle_area():
  global radius
  area = math.pi * radius ** 2
  return area
  
def circle_circumference():
  global radius
  circumferece = 2 * math.pi * radius
  return circumferece

radius = float(input("Please type in the radius of the circle: "))

area = circle_area()
circumference = circle_circumference()
print("The circle has an area of", round(area,2), "\nwith a circumference of", round(circumference,2))

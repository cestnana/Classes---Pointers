# from turtle import color


class MyColor:
  def __init__(self, color):
    self.color = color
    
  def get_color(self):
    return  self.color
  
  def set_color(self, color):
    self.color = color
    

color_one = MyColor('red')
color_two = MyColor('blue')

print('Color one is', color_one.get_color())
print('Color two is', color_two.get_color())

color_one.set_color('yellow')

print('Color one is now', color_one.get_color())
print('Color two is still', color_two.get_color())
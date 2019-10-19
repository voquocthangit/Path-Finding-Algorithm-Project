import arcade
from Graph2D import Graph2D
from Switcher import Switcher
from Graphic2D import Graphic2D
class IOHandler:
  def __init__(self):
    pass
  
  def read_file(self,path):
    with open(path) as input_file:
      # Get all lines from input file
      lines = [line for line in input_file]
    
      # Convert line to attribute
      width, height = [int(x) for x in lines[0].split()]
    
      # Start, End , Pick-up points
      points = [int(x) for x in lines[1].split()]
      length = len(points)
      x = [points[i] for i in range(length) if i % 2 == 0]
      y = [points[i] for i in range(length) if i % 2 == 1]
    
      start = (x[0], y[0])
      end = (x[1], y[1])
      pick_up_points = [(x[i], y[i]) for i in range(2, length//2)]
    
      # Get polygons
      length = len(lines)
      polygons = [[int(x) for x in lines[i].split()] for i in range(3, length)]
    
      # Convert type of polygons from list of list to list of list of tuple
      new_polygons = []
      for polygon in polygons:
        temp_polygon = []
      
        for i in range(len(polygon)):
          if i % 2 == 0:
            x = polygon[i]
          
          if i % 2 == 1:
            y = polygon[i]
            temp_polygon.append((x, y))
          
        new_polygons.append(temp_polygon)
    return width, height, start, end, new_polygons, pick_up_points

  def display_menu(self,number_of_levels): 
    for i in range(number_of_levels):
      level = i+1
      display_level = str(level)+'. level '+str(level)
      print(display_level)
  
  def handle_input(self):
    level = input('Level: ')
    print ('\n')
    file_path = input("Enter your file path: ")
    print('\n')

    self.width,self.height,self.start,self.end,self.polygons,self.pick_up_points = self.read_file(file_path)

    self.graph2D = Graph2D(self.width+1,self.height+1)
    self.graph2D.polygons_to_coordinate(self.polygons)

    switcher = Switcher(self.graph2D,self.start,self.end)
    result = switcher.execute(level)
    return result

  def handle_output(self,path): 
    window = Graphic2D(self.width,self.height)
    window.setup()
    window.draw_output(self.start,self.end,self.graph2D.points_to_polygons(self.polygons),self.pick_up_points,path)
    arcade.run()

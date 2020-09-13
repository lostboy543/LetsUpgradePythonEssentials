import math
pi = math.pi 
class cone:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        
        
    def volume(self):
        r=self.radius
        h=self.height
        print( "Volume Of Cone : ", (1 / 3) * pi * r * r * h) 
        
    def surfaceArea(self):
        r=self.radius
        h=self.height
        print( "Surface Area : ", pi * r * math.sqrt(h*h+r*r) + pi * r * r  )
           
cone1=cone(5,10)
cone1.volume()
cone1.surfaceArea()


        
import math

class circle:
    def __init__(self,r):
        self.radius = r
    def calculate_area(self):
        return self.radius**2 *math.pi
    def calculate_surface(self):
        return self.radius*2 *math.pi

day_1 = circle(80)

print(f'masahat barabar ast ba:{day_1.calculate_area()}')
print(f'mohit barabar ast ba:{day_1.calculate_surface()}')




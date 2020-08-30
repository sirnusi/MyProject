class New():
    def __init__(self, radius):
        self.radius = radius
    
    def get_radius(self):
        return self.radius * self.radius
    
n = New(5)
print(n.get_radius())

class Turtle:
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s
    
    def go_up(self):
        self.y += self.s
        
    def go_down(self):
        self.y -= self.s
        
    def go_left(self):
        self.x -= self.s
        
    def go_right(self):
        self.x += self.s
        
    def evolve(self):
        self.s += 1
        
    def degrade(self):
        if self.s <= 1:
            print("Шаг не может быть меньше или равен нулю")
        self.s -= 1
        
    def count_moves(self, x2, y2):
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)
        return max(dx, dy) // self.s + (max(dx, dy) % self.s > 0)

turtle = Turtle()

moves_to_target = turtle.count_moves(3, 7)
print(moves_to_target)
from operations import Operations

class Game_manager:
    def __init__(self):
        print("gm is on")
        
        self.robots = []
        self.walls = []
        self.floors = []

        self.allObj = [self.robots, self.walls, self.floors]

        self.op = Operations()  # Создаём объект операций

    def cycle(self, screen):
        # Отрисовываем стены
        for wall in self.walls:
            self.op.draw(screen, wall)

        # Отрисовываем пол
        for floor in self.floors:
            self.op.draw(screen, floor)

        # Обрабатываем состояние и отрисовываем роботов
        for robot in self.robots:
            self.op.state(robot,self.allObj)
            self.op.draw(screen, robot)
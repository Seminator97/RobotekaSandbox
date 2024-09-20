import pygame
import random


class Objects:
    def __init__(self, x, y, image, isImpassable, type):
        self.x = x // 48  # Координаты в клетках
        self.y = y // 48
        self.image = pygame.image.load(f"textures/{image}")
        self.isImpassable = isImpassable  # Свойство непроходимости
        self.type = type  # Тип объекта (стена, робот и т.д.)
        self.isIdlemoving = False
        self.timer = random.randint(100, 200)



   
        
    
    
        





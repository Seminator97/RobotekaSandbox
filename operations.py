import pygame
import random

class Operations:
    def __init__(self):
        print("operations online")
        
    def draw(self, screen, object):
        object.image = pygame.transform.scale(object.image, (48, 48))
        screen.blit(object.image, (object.x * 48, object.y * 48))

    def state(self, object, allObj):
        object.timer -= 1
        # Движение без дела
        if object.isIdlemoving:
            self.moveIdle(object, allObj)
            object.isIdlemoving = False
            object.timer = random.randint(50, 100)
            return
        
        # Если стоит без дела
        if object.timer == 0:
            object.isIdlemoving = True
            object.timer = random.randint(50, 100)
            return
            
    def moveIdle(self, object, allObj):
        direction = random.choice([(1, 0), (0, 1), (-1, 0), (0, -1)])  # Возможные направления
        moveX, moveY = direction 
        newX = object.x + moveX
        newY = object.y + moveY
        if self.canMoveTo(newX, newY,allObj):
            object.x += moveX
            object.y += moveY

    def canMoveTo(self, newX, newY, allobj):
        for obj in allobj:
            for obj2 in obj:
                if obj2.x == newX and obj2.y == newY and obj2.isImpassable:
                    return False
        return True

    def is_position_occupied(self,gm, x, y):
        x = x // 48
        y = y // 48
        for obj in gm.walls + gm.robots:
            if obj.x == x and obj.y == y:
                print("cannot build")
                return True
        return False
    
    def delete(self,x,y,gm):
        c = 0
        for obj in gm.allObj:
            for obj2 in obj:
                if obj2.x == x and obj2.y == y:
                    obj.remove(obj2)

                    
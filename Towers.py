import pygame
import Game
Tower_size=50
class Kanon():

    def __init__(self,pos,num) -> None:
        self.screen = Game.screen
        self.image = Game.images["Kanon"]
        self.pos = pos
        self.space = 1
        self.cost=100
        self.damge = 1
        self.upgrade = 0
        self.num = num

    def Upgrade(self):
        self.upgrade+=1
    
    def get_num(self):
        return self.num

    def get_pos(self):
        return self.pos
    
    def check_need_flip(self,image):
        if self.pos[1] > 350:
            if self.pos[0] < 1150:
                return pygame.transform.flip(image,True,False)
            return image
        return pygame.transform.flip(image,False,True)

    def draw(self):
        self.screen.blit(pygame.transform.scale(self.check_need_flip(self.image), (Tower_size*self.space,Tower_size*self.space)), (int(self.pos[0]-Tower_size/2),int(self.pos[1]-Tower_size/2)))


class MageTower():
    
    def __init__(self,pos,num) -> None:
        self.screen = Game.screen
        self.image = Game.images["MageTower"]
        self.pos = pos
        self.space = 2
        self.damge = 10
        self.cost=100
        self.upgrade = 0
        self.num = num

    def Upgrade(self):
        self.upgrade+=1

    def get_num(self):
        return self.num

    def get_pos(self):
        return self.pos
    
    def check_need_flip(self,image):
        if self.pos[1] > 350:
            return image
        return pygame.transform.flip(image,True,False)

    def draw(self):
        self.screen.blit(pygame.transform.scale(self.check_need_flip(self.image), (Tower_size*self.space,Tower_size*self.space)), (int(self.pos[0]-Tower_size/2),int(self.pos[1]-Tower_size/2)))

class Katapult():
    
    def __init__(self,pos,num) -> None:
        self.screen = Game.screen
        self.image=Game.images["Katapult"]
        self.pos = pos
        self.space = 2
        self.damge = 10
        self.cost=100
        self.upgrade = 0
        self.num=num

    def Upgrade(self):
        self.upgrade+=1

    def get_num(self):
        return self.num

    def get_pos(self):
        return self.pos

    def check_need_flip(self,image):
        if self.pos[1] > 350:
            return image
        return pygame.transform.flip(image,True,False)

    def draw(self):
        self.screen.blit(pygame.transform.scale(self.check_need_flip(self.image), (Tower_size*self.space,Tower_size*self.space)), (int(self.pos[0]-Tower_size/2),int(self.pos[1]-Tower_size/2)))
    
if __name__ == "__main__":
    Kanon().draw()
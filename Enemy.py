import pygame
from get_rgb_codes import RGB
import random
from Game import Height, screen
colors = RGB(True,None,False)[1]
class Bloons():

    def __init__(self,pos,num) -> None:
        self.Health = 1
        self.screen = screen
        self.upgrade=0
        self.pos = (1105,Height-25)
        self.color = random.choice(colors)
        self.num=num
        self.Path = [[1105,Height-25],[1105,350],[280,350],[280,0]]
    
    def get_num(self):
        return self.num

    def get_pos(self):
        return self.pos

    def draw(self,multiplier):
        pygame.draw.circle(self.screen,self.color,[int(self.pos[0]),int(self.pos[1])],25)
        self.change_pos(self.pos,multiplier)

    def change_pos(self,last_pos,multiplier):
        last_pos=list(last_pos)
        if last_pos[-1] > self.Path[1][-1]:
            last_pos[1]-=10.0*multiplier
        else:
            if last_pos[0] > self.Path[2][0]:
                last_pos[0]-=10.0*multiplier
            else:
                if last_pos[-1] > self.Path[3][-1]:
                    last_pos[-1]-=10.0*multiplier  
        self.pos=last_pos
        print(self.pos)
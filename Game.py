import pygame
import Enemy 
import platform
from Figurenverwaltung import Liste
from Towers import Kanon, Katapult, MageTower
import datetime as dt
pygame.init()
Width = 1750
Width_pic = 1500
Height = 1000
screen = pygame.display.set_mode((Width,Height))
images={"Kanon":pygame.image.load(".\Images\Kanone.png").convert_alpha(),"Katapult":pygame.image.load(".\Images\Katapult.png").convert_alpha(),"MageTower":pygame.image.load(".\Images\MageTower.png").convert_alpha()} if platform.system() == 'Windows' else {"Kanon":pygame.image.load("./Images/Kanone.png").convert_alpha(),"Katapult":pygame.image.load("./Images/Katapult.png").convert_alpha(),"MageTower":pygame.image.load("./Images/MageTower.png").convert_alpha()}
class Render():
    
    def __init__(self) -> None:
        self.colours = (0,0,255)
    
    def grid(self):
        blockSize = 50 #Set the size of the grid block
        for x in range(0, Width, blockSize):
            for y in range(0, Height, blockSize):
                self.draw_rect(self.colours,x,y,blockSize,blockSize)

    def draw_rect(self,colour,pos_x,pos_y,size_x,size_y):
        pygame.draw.rect(screen,colour,[pos_x,pos_y,size_x,size_y],1)

class Spielfeld():

    def __init__(self) -> None:
        self.r = Render()
        if platform.system() == 'Windows':
            self.image = pygame.image.load(".\Images\Map.jpg").convert_alpha()
        else:
            self.image = pygame.image.load("./Images/Map.jpg").convert_alpha()
        
    #list tower,list enemy, list towerpic
    def draw_board(self,lt,le,ltp):
        screen.blit(pygame.transform.scale(self.image, (Width_pic,Height)), (0,0))
        lt.Draw()
        le.Draw()
        le.Change_multiplier(lt.Length())
        ltp.Draw()
        #self.r.grid()

def main(): 
    done = False
    Figure="Kanon"
    S = Spielfeld()
    l_Towers = Liste()
    l_Enemies = Liste()
    l_Towers_pic = Liste()
    clock = pygame.time.Clock()
    pygame.display.flip()
    time = dt.datetime.now()
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                if event.key == pygame.K_1:
                    Figure = "Kanon"
                if event.key == pygame.K_2:
                    Figure = "Mage"
                if event.key == pygame.K_3:
                    Figure = "Katapult"
                if event.key == pygame.K_0:
                    Figure = "Enemey"
                if event.key == pygame.K_BACKSPACE:
                    if l_Towers.Length()>0:
                        print(l_Towers.LetzenEntfernen().get_num())
                    else:
                        print("No Tower in List")
                if event.key == pygame.K_DELETE:
                        l_Towers.Entferne_alle()
                        l_Enemies.Entferne_alle()
                        l_Enemies.Reset_multiplier()
                        print("No Towers")
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if Figure == "Kanon":
                    l_Towers.Hinzufügen(Kanon(pygame.mouse.get_pos(),l_Towers.Length()+1))
                elif Figure == "Mage":
                    l_Towers.Hinzufügen(MageTower(pygame.mouse.get_pos(),l_Towers.Length()+1))
                elif Figure == "Katapult":
                    l_Towers.Hinzufügen(Katapult(pygame.mouse.get_pos(),l_Towers.Length()+1))
                elif Figure == "Enemey":
                    l_Enemies.Hinzufügen(Enemy.Bloons(pygame.mouse.get_pos(),l_Enemies.Length()+1))
        S.draw_board(l_Towers,l_Enemies,l_Towers_pic)
        if l_Enemies.Outoffield() != None:
            l_Enemies.Hinzufügen(Enemy.Bloons((0,0),l_Enemies.Length()+1))
        pygame.display.update()
        clock.tick(100)
    pygame.quit()
if __name__ == "__main__":
    main()

from Listenelement import Abschluss
import Enemy
class Liste():

    def __init__(self) -> None:
        self.Erster = Abschluss()
        self.Tower_multiplier=1.0
        self.old_length=self.Length()

    def Hinzufügen(self,Figure):
        #Hintern Einfügen
        self.Erster=self.Erster.HintenEinfügen(Figure)

        #Vorne Einfügen
        # temp=DatenKnoten(Abschluss(),Figure)
        # temp.NächsterSetzen(self.Erster)
        # self.Erster = temp

    def Entfernen(self,key):
        self.Erster = self.Erster.Entfernen(key)

    def Entferne_alle(self):
        self.Erster=Abschluss()

    def Suchen(self,key):
        return self.Erster.Suchen(key)

    def Outoffield(self):
        outoffield= self.Erster.Outoffield()
        self.Entfernen(outoffield)
        return outoffield

    def LetzenEntfernen(self):
        d = self.Erster.LetzterGeben(None)
        if d != None:
            self.Entfernen(d.get_num())
            return d
        return None

    def Length(self):
        return self.Erster.Length()
        
    def Draw(self):
        if type(self.Erster) != Abschluss:
            if type(self.Erster.Tower) == Enemy.Bloons:
                self.Erster.Draw_Enemy(self.Tower_multiplier)
                return
        self.Erster.Draw()

    def Change_multiplier(self,length_of_towers):
        if self.old_length != length_of_towers:
            self.Tower_multiplier += length_of_towers/10000
        self.old_length=length_of_towers

    def Reset_multiplier(self):
        self.Tower_multiplier=1.0


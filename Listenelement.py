from abc import ABC, abstractmethod
import Enemy
class Listenelement(ABC):

    def __init__(self) -> None:
        self.Erster = Abschluss()

    @abstractmethod 
    def HintenEinfügen(self): pass

    @abstractmethod
    def Suchen(self,key): pass

    @abstractmethod
    def Outoffield(self): pass

    @abstractmethod
    def NächsterSetzen(self,Nächster): pass
        
    @abstractmethod
    def LetzterGeben(self,Tower): pass

    @abstractmethod
    def Draw(self): pass

    @abstractmethod
    def Draw_Enemy(self,multiplier): pass
        
    @abstractmethod
    def Entfernen(self,num): return

    @abstractmethod
    def Length(self): return 
        
    
class Abschluss(Listenelement):

    def __init__(self) -> None: return

    def HintenEinfügen(self,E): return DatenKnoten(self,E)

    def NächsterSetzen(self,Nächster): return

    def LetzterGeben(self,Tower): return Tower

    def Suchen(self,key): return None

    def Outoffield(self): return

    def Draw(self): return

    def Draw_Enemy(self,multiplier): return

    def Length(self): return 0

    def Entfernen(self,num): return self

class DatenKnoten(Listenelement):
    
    def __init__(self,A,Element) -> None:
        self.Nächster = A 
        self.Tower = Element
        
    def HintenEinfügen(self,E):
        self.Nächster = self.Nächster.HintenEinfügen(E)
        return self

    def LetzterGeben(self,Tower):
        return self.Nächster.LetzterGeben(self.Tower)

    def Suchen(self,key):
        if self.Tower.get_num() == key:
            return self.Tower
        else:
            return self.Nächster.Suchen(key)

    def Outoffield(self):
        if type(self.Tower) == Enemy.Bloons:
            if self.Tower.get_pos()[-1] < 1:
                return self.Tower.get_num()
            else:
                return self.Nächster.Outoffield()
        return

    def NächsterSetzen(self,Nächster):
        self.Nächster = Nächster

    def Entfernen(self,Num):
        if Num == self.Tower.get_num():
            return self.Nächster
        else:
            self.Nächster = self.Nächster.Entfernen(Num)
            return self

    def Length(self):
        return self.Nächster.Length()+1
        
    def Draw_Enemy(self,multiplier):
        self.Tower.draw(multiplier)
        self.Nächster.Draw_Enemy(multiplier)

    def Draw(self):
        self.Tower.draw()
        self.Nächster.Draw()


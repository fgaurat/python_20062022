


from ICalcGeo import ICalcGeo


class Rectangle(ICalcGeo):
    cpt = 0

    def __init__(self,longueur,largeur) -> None:
        self._longueur = longueur
        self._largeur = largeur
        Rectangle.cpt+=1

    @property
    def longueur(self):
        return self._longueur
    @property
    def largeur(self):
        return self._largeur

    @longueur.setter
    def longueur(self,longueur):
        self._longueur = longueur
    
    @largeur.setter
    def largeur(self,largeur):
        self._largeur = largeur

    def calc_surface(self):
        return self._longueur*self._largeur

    def __str__(self) -> str:
        return f"Rectangle, {self._longueur=}, {self._longueur=}"

    def __int__(self):
        return self.get_surface()

    def __eq__(self, __o: object) -> bool:
        result = False
        if self.longueur == __o.longueur and self.largeur == __o.largeur:
            result = True
        
        return result

    
    def __del__(self):
        print("destructeur Rectangle")
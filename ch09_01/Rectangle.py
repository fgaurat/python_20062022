


class Rectangle:
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

    def get_surface(self):
        return self._longueur*self._largeur

    def __str__(self) -> str:
        return f"Rectangle, {self._longueur=}, {self._longueur=}"

    def __int__(self):
        return self.get_surface()
class Csucs:
    """
        Egy csúcsot reprezentál amelynek két attribútumja van amelyek a megjelenítéskor szükségesek
    
    """
    def __init__(self,cord_x,cord_y):
        """Beállítja a csúcs koordinátáit"""
        self.koord_x=cord_x
        self.koord_y=cord_y
    
    def __str__(self):
        """Csúcs szöveggé konvertálása:"x: szam, y:szam" formátumban"""
        return "x: {}, y: {}".format(self.koord_x,self.koord_y)
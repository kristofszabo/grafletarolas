from graf import Graf
from menu import Menu
class Main:
    @staticmethod
    def main():
        """Létrehoz egy gráfot és azt átadja egy menü objektnek és meghívja a menü futtat metódusát"""
        graf=Graf()
        myMenu=Menu(graf)
        myMenu.futtat()

Main.main()
    



            
        

import os
from svgwriter import SvgWriter
class Menu:
    """A menüt kezelő és megjelenítő osztály
    """
    def __init__(self,graf):
        """Beállítja a kezdő gráfot és a menüben megtalálható opciókat
        
        Arguments:
            graf {Graf} -- A gráf ami állítódni fog a menün keresztül
        """
        self.opciok=[
            "Csúcs hozzá adása a gráfhoz",
            "Csúcs törlése a gráfból",
            "Csúcs koordinátáinak módosítása",
            "Él felvétele a gráfba",
            "Él törlése a gráfból",
            "Él súlyának módosítása",
            "Legrövidebb út keresése",
            "Gráf exportálása",
            "Gráf importálása",
            "Gráf kiírása",
            "Gráf kirajzolása"
            ]
        self.graf=graf
    
    def kiir(self):
        """A console-ra kiírja a szomszédossági mátrixát a gráfnak"""
        for i in range(len(self.opciok)):
            print("{}. {}".format(i+1,self.opciok[i]))

    def beolvas(self):
        """Beolvas a szabványos bemenetről egy számot és ha a menük intervallumán kívül lévő számot -1et dob"""
        try:
            szam=int(input())
        except:
            return -1
        if szam<1 or szam>len(self.opciok):
            return -1
        return szam
    
    def futtat(self):
        """Főmenü futtatása"""
        while True:
            try:
                self.kiir()
                bemenet=self.beolvas()
                if(bemenet==1):
                    koord_x=int(input("Adja meg az új csúcs x koordinátáját: "))
                    koord_y=int(input("Adja meg az új csúcs y koordinátáját: "))
                    self.graf.csucs_hozza_ad(koord_x,koord_y)
                elif(bemenet==2):
                    csucsszam=int(input("Adja meg a törölni való csúcsot: "))
                    self.graf.csucs_torol(csucsszam)
                elif(bemenet==3):
                    csucsindex=int(input("Adja meg a módosítani való csúcs indexét: "))
                    uj_koord_x=int(input("Adja meg a csúcs új x koordinátáját: "))
                    uj_koord_y=int(input("Adja meg a csúcs új y koordinátáját: "))
                    self.graf.csucs_modosit(csucsindex,uj_koord_x,uj_koord_y)
                elif(bemenet==4):
                    kezdo=int(input("Adja meg a kezdő csúcs indexét: "))
                    vege=int(input("Adja meg a vég csúcs indexét: "))
                    suly=int(input("Adja meg az él súlyát: "))
                    self.graf.el_hozza_ad(kezdo,vege,suly)
                elif(bemenet==5):
                    kezdo=int(input("Adja meg a kezdő csúcs indexét: "))
                    vege=int(input("Adja meg a vég csúcs indexét: "))
                    self.graf.el_torol(kezdo,vege)
                elif(bemenet==6):
                    kezdo=int(input("Adja meg a kezdő csúcs indexét: "))
                    vege=int(input("Adja meg a vég csúcs indexét: "))
                    suly=int(input("Adja meg az él új súját: "))
                    self.graf.el_suly_modosit(kezdo,vege,suly)
                    
                elif(bemenet==7):
                    kezdo=int(input("Adja meg a kezdő csúcs indexét: "))
                    vege=int(input("Adja meg a vég csúcs indexét: "))
                    ut=self.graf.legrovidebb_ut(kezdo,vege)
                    if(ut==None):
                        print("Nincs ilyen út")
                    else:
                        print(ut)
                elif(bemenet==8):
                    fajlnev=input("Adja meg a fájlnevet amibe menteni szeretne")
                    self.graf.mentes(fajlnev)
                elif(bemenet==9):
                    fajlnev=input("Adja meg a fájlnevet amiből betölteni szeretne")
                    self.graf.betolt(fajlnev)
                elif(bemenet==10):
                    self.graf.kiir()
                elif(bemenet==11):
                    fajlnev=input("Adja meg a leendő svg fájl nevét: ")
                    svg =SvgWriter(fajlnev)
                    svg.create(self.graf)
                    os.system('cmd /c "explorer "'+os.getcwd()+'\\'+fajlnev+'""')
                elif(bemenet==-1):
                    return
            except:
                print("Hiba történt")
                continue
            



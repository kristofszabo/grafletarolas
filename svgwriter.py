from sys import maxsize

class SvgWriter:
    def __init__(self,fajlnev):
        """Beállítja az alap file nevet amit használni szeretne a felhasználó
        
        Arguments:
            fajlnev {string} -- Fájlnév
        """
        self.fajlnev=fajlnev
    
    def create(self,graf):
        """Egy gráfból létrehoz egy svg file-t a beállított file néven
        
        Arguments:
            graf {Graf} -- A gráf amit megjelenít
        """
        with open(self.fajlnev,"w+") as f:
            f.write('<svg width="600" height="480" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">\n')
            for honnanindex,sor in enumerate(graf.elmatrix):
                for hovaindex,oszlop in enumerate(sor):
                    if(honnanindex==hovaindex):
                        continue
                    if(oszlop!=maxsize):
                        f.write(SvgWriter.vonal_csucsok_kozott(graf.csucsok[honnanindex],graf.csucsok[hovaindex]))
            for csucs_index,csucs in enumerate(graf.csucsok):
                f.write(SvgWriter.create_circle(csucs,csucs_index))
            f.write('</svg>')

    @staticmethod
    def create_circle(csucs,csucsertek):
        """Egy SVG kódot ad vissza amiben található egy kör és a csúcs értékének kódja
        
        Arguments:
            csucs {Csucs} -- A megjelenítendő csúcs
            csucsertek {Value} -- A csúcson szerelpő érték

        Returns:
            string -- Egy svg kör benne a megjelenítendő szöveggel
        """
        r=20
        circle="<circle cx='{}' cy='{}' r='{}' stroke='black' fill='brown'/>\n".format(csucs.koord_x,csucs.koord_y,r)
        text="<text x='{}' y='{}' fill='blue'>{}</text>\n".format(csucs.koord_x-r/2,csucs.koord_y,csucsertek)
        return circle+text
    
    @staticmethod
    def vonal_csucsok_kozott(kezdocsucs,vegcsucs):
        """Készít egy svgnek megfelelő részletet ami egy vonalat fog képezni 2 csúcs között
        
        Arguments:
            kezdocsucs {Csucs} -- A csúcs ahonnan indul a vonal
            vegcsucs {Csucs} -- A csúcs ahova megy a vonal
        
        Returns:
            string -- Egy svg vonal
        """
        return "<line x1='{}' y1='{}' x2='{}' y2='{}' style='stroke:rgb(255,0,0);stroke-width:3'/>\n".format(kezdocsucs.koord_x,kezdocsucs.koord_y,vegcsucs.koord_x,vegcsucs.koord_y)
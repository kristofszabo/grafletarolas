from csucs import Csucs
from sys import maxsize
class Graf:
    """Egy gráfot reprezentál élmátrix és csúcsok listájának használatával
    """
    def __init__(self):
        """Beállítja üres tömbökre a gráf élmátrixát és a csúcsok listáját
        """
        self.elmatrix=[]
        self.csucsok=[]
    
    def csucs_hozza_ad(self,koord_x,koord_y):
        """Hozzá ad egy csúcsot a gráfhoz és beállítja az x és y koordinátáit
            paraméterek:
            koord_x: Az új csúcs x koordinátája
            koord_y: Az új csúcs y koordinátája
            """
        self.csucsok.append(Csucs(koord_x,koord_y))
        if(len(self.elmatrix)==0):
            self.elmatrix.append([maxsize])
            return
        self.elmatrix.append([maxsize]*len(self.elmatrix))
        for sor in self.elmatrix:
            sor.append(maxsize)

    def csucs_torol(self,index):
        """Törli az adott indexű csúcsot a gráfból és azon éleket amelyek rá mutattak előtte
            params:
            index = A csúcs gráfban lévő indexe
            """
        for i in range(len(self.elmatrix)):
            del self.elmatrix[i][index]
        del self.elmatrix[index]
        del self.csucsok[index]
    
    def csucs_modosit(self,index,uj_koord_x,uj_koord_y):
        """Módosítja az adott indexen lévő csúcs koordinátáit
            paraméterek:
            index: Csúcs indexe
            uj_koord_x: A csúcs új x koordinátája
            uj_koord_y: A csúcs új y koordinátája
        """
        self.csucsok[index].koord_x=uj_koord_x
        self.csucsok[index].koord_y=uj_koord_y

    def mentes(self,fajlnev):
        with open(fajlnev,"wt") as f:
            f.write(str(len(self.csucsok))+"\n")
            for csucs in self.csucsok:
                f.write("{} {}".format(csucs.koord_x,csucs.koord_y)+"\n")
            for sor in self.elmatrix:
                f.write(" ".join(map(str,sor))+"\n")



    def betolt(self,fajlnev):
        """Betölt egy korábban elkészített fileból egy gráfot és azt teszi aktuálissá
        
        Arguments:
            fajlnev {string} -- Fájl neve
        """
        self.elmatrix=[]
        self.csucsok=[]
        with open(fajlnev,"rt") as f:
            csucsokszama=int(f.readline())
            for _ in range(csucsokszama):
                csucs=f.readline().split(" ")
                self.csucs_hozza_ad(int(csucs[0]),int(csucs[1]))
            szamlalo=0
            for sor in f:
                ertekek=sor.split(" ")
                for j,suly in enumerate(ertekek):
                    self.elmatrix[szamlalo][j]=int(suly)
                szamlalo+=1



    
    def el_hozza_ad(self,kezdoindex,vegindex,suly):
        """Hozzá ad egy irányított élet a gráfhoz
        
        Arguments:
            kezdoindex {int} -- Melyik indexű csúcsból indul az él
            vegindex {int} -- Melyik indexű csúcsra mutat az él
            suly {int} -- A hozzáadott él súlya
        """
        if(kezdoindex==vegindex): 
            return
        self.elmatrix[kezdoindex][vegindex]=suly

    def el_torol(self,kezdoindex,vegindex):
        """A default értékre(lehetséges max változóértékre) állítja az él súlyát az élmátrixban
        
        Arguments:
            kezdoindex {int} -- Az él kezdő csúcsának indexe
            vegindex {int} -- Az él cél csúcsának indexe
        """
        self.elmatrix[kezdoindex][vegindex]=maxsize
    
    def el_suly_modosit(self, kezdoindex,vegindex,suly):
        """Megváltoztatja az él súlyát 
        
        Arguments:
            kezdoindex {int} -- Az él kezdő indexe
            vegindex {int} -- Az él cél indexe
            suly {int} -- Az új élsúly
        """
        
        self.elmatrix[kezdoindex][vegindex]=suly
    


    def legrovidebb_ut(self,kezdoindex,vegindex):
        """Vissza adja a legrövidebb utat a kezdő csúcsból a célcsúcsba.

        Arguments:
            kezdoindex {int} -- Kezdő csúcs indexe
            vegindex {int} -- Cél csúcs indexe
        
        Returns:
            List<int> -- A lista a kezdő élből a cél élbe
            Ha nincs ilyen None-t ad vissza
        """
        if(len(self.csucsok)==0):
            return None
        if(kezdoindex==vegindex):
            return [0]
        dist=len(self.csucsok)*[maxsize]
        previous=[None]*len(self.csucsok)
        dist[kezdoindex]=0
        previous[kezdoindex]=kezdoindex
        q=[]
        for i in range(0,len(self.csucsok)):
            q.append(i)
        while len(q)!=0:
            min_index=Graf.minimum_index_valasztottakbol(dist,q)
            u=min_index
            q.remove(min_index)
            for i,tav in enumerate(self.elmatrix[u]):
                if(u==i or tav==maxsize):
                    continue
                alt=dist[u]+tav
                if alt<dist[i]:
                    dist[i]=alt
                    previous[i]=u
        ut=[vegindex]
        actual=vegindex
        while actual!=kezdoindex:
            if(actual==None):
                return
            actual=previous[actual]
            ut.append(actual)
        ut.reverse()
        return ut
            

    
    def kiir(self):
        """Ki írja az élmátrixot a szabványos kimenetre és a csúcsokhoz tartozó koordinátákat"""
        for i in range(len(self.csucsok)):
            print("{}. Csúcs: {}".format(i,self.csucsok[i]))
        print("{:11}".format(" "),end=' ')
        for i in range(len(self.elmatrix)):
            print("{:11}".format(i),end=" ")
        print()
        for i in range(len(self.elmatrix)):
            print("{:11}".format(i), end=" ")
            for oszlop in self.elmatrix[i]:
                print("{:11}".format(oszlop),end=" ")
            print()


    @staticmethod
    def minimum_index_valasztottakbol(tavolsagok,lehetsegesek):
        """Megkeresi a legkissebb elemet bizonyos elemek közül és vissza adja az indexet ami hozzá tartozik.
        
        Arguments:
            tavolsagok {List<int>} -- Melyek közt kell keresni
            lehetsegesek {List<int>} -- Mely elemek lehetségesek
        
        Returns:
            int -- A legutoljára szerepelt legkissebb elem indexe
        """
        minimum=maxsize
        lehetindex=lehetsegesek[0]
        for lehet in lehetsegesek:
            if(tavolsagok[lehet]<minimum): 
                minimum=tavolsagok[lehet]
                lehetindex=lehet
        return lehetindex
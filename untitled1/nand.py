from arvore import *
from copy import deepcopy

class Nand:
    def __init__(self,n,seq):
        self.n = n
        self.seq = seq
        self.f = 2 ** (self.n - 1)
        self.lista = []
        self.arvore = ''
        self.criaLista()
        self.listar()
        self.arv()

    def criaLista(self):
        a=0
        while(a!=self.n-1):
            self.lista.append([])
            a+=1
        self.lista.append(self.seq)

    def listar(self):
        b = self.n - 1
        while(b != 0):
            listaAux = []
            c = len(self.lista[b])
            while(c != 0):
                c-=1
                r1 = self.lista[b][c]
                c-=1
                l1 = self.lista[b][c]
                c1 = int(not(r1 and l1))
                listaAux.insert(0,c1)
            b-=1
            self.lista[b]=listaAux

    def arv(self):
        b = self.n - 1
        listaAux = deepcopy(self.lista)
        while(b!=0):
            c = len(self.lista[b]) - 1
            while(c > 0):
                r=listaAux[b][c]
                c-=1
                l=listaAux[b][c]
                if(c==0):
                    listaAux[b-1][0] = arvore(listaAux[b-1][0],l,r)
                else:
                    listaAux[b-1][int(c/2)] = arvore(listaAux[b-1][int(c/2)],l,r)
                c-=1
            b-=1
        self.arvore = listaAux[0][0]

    def printarLista(self):
        b = 0
        while (b != len(self.lista)):
            print(self.lista[b])
            b += 1

        #while(b>=0):










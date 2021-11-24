import csv
from datetime import datetime
from collections import namedtuple
'''
Empezaremos creando lo principal, su función de lectura, nos será de gran ayuda para poder trabajar bien con el resto del proyecto
'''
Ethereum=namedtuple('Ethereum','Date, Price,Open, High, Low, Vol, Change, Problemas, Paises')
def funcion_lectura(fichero):
    ethereum=[]
    with open(fichero ,encoding='utf-8') as f:
        lector= csv.reader(f)
        next(lector)
        for Date, Price, Open, High, Low, Vol, Change, Problemas, Paises in lector:
            Date= datetime.strptime(Date,'%b %d, %Y')
            Price=float(Price)
            Open= float(Open)
            High= float(High)
            Low= float(Low)
            Vol= float(Vol)
            Change= float(Change) #preguntar profesor
            Problemas= bool(Problemas)
            Paises= str(Paises)
            tupla=Ethereum(Date, Price, Open, High, Low, Vol, Change, Problemas,Paises)
            ethereum.append(tupla)
    return ethereum